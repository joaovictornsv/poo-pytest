from .base import BaseAppException
from src.app.constants import HttpStatusCode

class NotFoundException(BaseAppException):
    def __init__(self, message):
        super().__init__(message, HttpStatusCode.NOT_FOUND.value)
