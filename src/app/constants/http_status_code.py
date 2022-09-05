from enum import Enum


class HttpStatusCode(Enum):
    GET = (200,)
    POST = (201,)
    NOT_FOUND = 404
