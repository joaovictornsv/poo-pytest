from uuid import uuid4
from src.app.validation import Validator
from src.app.validation.schemas import ProductSchema


class Product:
    def __init__(self, name: str, price: float):
        self.__id = str(uuid4())
        self.__name = name
        self.__price = price
        self.__validate()

    # pylint: disable=C0103
    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    def __validate(self):
        validator = Validator()
        validator.validate(
            ProductSchema(), {"name": self.__name, "price": self.__price}
        )
