import colander
from src.app.exceptions import BadRequestException


class Validator:
    def validate(self, schema: colander.SchemaNode, data: dict):
        try:
            return schema.deserialize(data)
        except colander.Invalid as e:
            first_error = self.__get_first_error(e)
            error_message = self.__gen_error_message(first_error)
            raise BadRequestException(error_message)

    def __get_first_error(self, err: colander.Invalid):
        errors = err.asdict()
        first_error = list(errors.items())[0]
        error_dict = {"field": first_error[0], "message": first_error[1]}
        return error_dict

    def __gen_error_message(self, error_dict):
        field = error_dict["field"]
        message = error_dict["message"]

        error_message = f'Invalid field "{field}": {message}'
        return error_message
