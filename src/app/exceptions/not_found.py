from src.app.constants import HttpStatusCode
from .base import BaseAppException


class NotFoundException(BaseAppException):
    def __init__(self, message):
        super().__init__(message, HttpStatusCode.NOT_FOUND.value)
