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
        status_code = renderer_context['response'].status_code
        response = {
            'code': status_code,
            'error': False,
            'error_message': None,
            'data': data,
        }
        print('Data:')
        print(data)
        if data.get('results', None) is not None:
            return json.dumps({
                self.pagination_object_label: data['results'],
                self.pagination_count_label: data['count'],
                self.pagination_previous_label: data['previous'],
                self.pagination_next_label: data['next'],
            })
        # If the view throws an error, 'data' will contain an 'errors' key
        elif data.get('error', None) is not None and data['error']:
            return super(PyRestJSONRenderer, self).render(data)
        else:
            return json.dumps({
                self.object_label: data,
            })
