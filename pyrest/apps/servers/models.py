from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _


class Server(models.Model):

    class Meta:
        ordering = ['id']

    class ServerStatus(models.TextChoices):
        STARTING = 'STG', 'STARTING'
        WAITING = 'WAG', 'WAITING'
        STARTED = 'STD', 'STARTED'
        ENDING = 'ENG', 'ENDING'
        ENDED = 'END', 'ENDED'

    def __init__(self, *args, **kwargs):
        super(Server, self).__init__(*args, **kwargs)
        self._old = {}
        self._old['status'] = self.status
        self._old['end_time'] = self.end_time

    name = models.CharField(db_index=True, max_length=24)
    server_type = models.CharField(max_length=16)
    ip = models.GenericIPAddressField(protocol='IPv4')
    port = models.PositiveIntegerField(validators=[
        MaxValueValidator(65535)
    ])
    status = models.CharField(choices=ServerStatus.choices, default=ServerStatus.STARTING, max_length=3)
    creation_time = models.DateTimeField(editable=False, auto_now_add=True)
    end_time = models.DateTimeField(editable=True, null=True)

    def save(self, *args, **kwargs):
        if self._old['end_time'] and self._old['end_time'] != self.end_time:
            raise ValidationError(_('Cannot redefine field end_time'))
        super(Server, self).save(*args, **kwargs)
        self._old_end_time = self.end_time
