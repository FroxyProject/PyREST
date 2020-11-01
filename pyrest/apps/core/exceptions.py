import logging

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import exceptions, views


logger = logging.getLogger(__name__)


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
    if isinstance(response.data, list):
        error_message = response.data
    elif 'detail' in response.data:
        error_message = response.data['detail']
    else:
        error_message = response.data
    response.data = {
        'exception': error_message,
    }

    # Check if it's an error 500
    # TODO Find a better place to put this error
    if response.status_code >= 500:
        logger.error('Got error %d', response.status_code)
        logger.error('Response:')
        logger.error(response)
        logger.error('Original error:')
        logger.error(exc)
    return response
