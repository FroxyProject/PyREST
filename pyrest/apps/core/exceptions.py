from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import exceptions, views


def exception_handler(exc, context):
    response = views.exception_handler(exc, context)
    if response is None:
        # From here, check for each different exceptions
        if isinstance(exc, ValidationError):
            # Usually thrown by ´is_valid(raise_exception=True)´
            new_exc = exceptions.ParseError(str(exc))
        elif isinstance(exc, ObjectDoesNotExist):
            # Not found
            new_exc = exceptions.NotFound(str(exc))
        elif isinstance(exc, Exception):
            # Unknown exception
            new_exc = exceptions.APIException(str(exc))
        else:
            new_exc = exceptions.APIException('Unknown exception!')
        response = views.exception_handler(new_exc, context)
    if response is not None:
        if isinstance(response.data, list):
            return response
        response.data = make_response(response.data['detail'] if 'detail' in response.data else response.data, response.status_code)

    # Check if it's an error 500
    if response.status_code >= 500:
        print('Got error %d' % (response.status_code))
        print(response)
        print('Original error:')
        print(exc)
    return response


def make_response(error_message, status_code):
    return {
        'error': True,
        'error_message': error_message,
        'status_code': status_code,
    }
