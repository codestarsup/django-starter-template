from rest_framework import status
from rest_framework.exceptions import APIException


class CustomAPIException(APIException):
    def __init__(
        self,
        error_message="Error",
        error_data=None,
        status_code=status.HTTP_400_BAD_REQUEST,
        **kwargs
    ):
        self.error_message = error_message
        self.error_data = error_data
        self.status_code = status_code
        super().__init__(**kwargs)


class DataInvalidException(CustomAPIException):
    ...


class MaximumLimitException(CustomAPIException):
    ...
