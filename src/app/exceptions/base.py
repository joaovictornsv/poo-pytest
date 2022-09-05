class BaseAppException(Exception):
    def __init__(self, message, code):
        super().__init__(message, code)
        self._message = message
        self._code = code

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message
