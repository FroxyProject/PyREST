from ..core.renderers import PyRestJSONRenderer


class ServerJSONRenderer(PyRestJSONRenderer):
    object_label = 'server'
    pagination_object_label = 'servers'
    pagination_count_label = 'count'
