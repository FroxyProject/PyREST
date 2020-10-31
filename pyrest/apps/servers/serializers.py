from rest_framework import serializers

from .models import Server


class ServerSerializer(serializers.ModelSerializer):
    """
        The Output serializer.\n
        This is the data that we'll return when we want to have informations about a server
    """
    # creationTime = serializers.SerializerMethodField(method_name='get_creation_time')
    # endTime = serializers.SerializerMethodField(method_name='get_end_time')

    class Meta:
        model = Server
        fields = ['id', 'name', 'server_type', 'ip', 'port', 'status', 'creation_time', 'end_time']

    # def get_creation_time(self, instance):
    #     return instance.creation_time.isoformat()

    # def get_end_time(self, instance):
    #     return instance.end_time.isoformat()


class ServerInputSerializer(serializers.Serializer):
    """
        The Input used to identify a unique server.\n
        This is useful to check if the id passed by the client is valid.\n
        If it's not valid, a call to `is_valid(raise_exception=True)` will throw an exception
    """
    id = serializers.IntegerField(min_value=0)
