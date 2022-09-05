from uuid import uuid4


class Product:
    def __init__(self, name: str, price: float):
        self.__id = str(uuid4())
        self.__name = name
        self.__price = price

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
