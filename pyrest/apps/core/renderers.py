import json

from rest_framework.renderers import JSONRenderer


class PyRestJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'
    pagination_object_label = 'objects'
    pagination_count_label = 'count'
    pagination_previous_label = 'previous'
    pagination_next_label = 'next'

    def render(self, data, media_type=None, renderer_context=None):
        renderer_context = renderer_context or {}

        response = renderer_context['response']
        status_code = response.status_code
        # If there is an error, show it
        if response.exception:
            dump = {
                'status_code': status_code,
                'error': data['exception'],
            }
        elif data.get('results', None) is not None:
            dump = {
                'status_code': status_code,
                self.pagination_object_label: data['results'],
                self.pagination_count_label: data['count'],
                self.pagination_previous_label: data['previous'],
                self.pagination_next_label: data['next'],
            }
        else:
            dump = {
                'status_code': status_code,
                self.object_label: data,
            }
        return json.dumps(dump)
