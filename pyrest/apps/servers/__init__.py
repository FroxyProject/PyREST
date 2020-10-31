from django.apps import AppConfig


class ServersAppConfig(AppConfig):
    name = 'pyrest.apps.servers'
    label = 'servers'
    verbore_name = 'Servers'


default_app_config = 'pyrest.apps.servers.ServersAppConfig'
