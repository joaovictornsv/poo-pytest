from src.app.constants import HttpStatusCode
from .base import BaseAppException


class BadRequestException(BaseAppException):
    def __init__(self, message):
        super().__init__(message, HttpStatusCode.BAD_REQUEST.value)
