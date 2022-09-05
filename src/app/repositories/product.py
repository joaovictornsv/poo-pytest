import copy
from typing import List
from src.app.entities import Product
from src.app.exceptions import NotFoundException
from src.app.constants import CartErrorMessages


class ProductRepository:
    def __init__(self):
        self.__items = []

    def create(self, product: Product) -> None:
        self.__items.append(product)

    def delete(self, product_id: str) -> None:
        found_product = False
        index_to_delete = 0

        for index, product in enumerate(self.__items):
            if product.id == product_id:
                found_product = True
                index_to_delete = index
                break

        if not found_product:
            raise NotFoundException(CartErrorMessages.PRODUCT_NOT_FOUND.value)

        self.__items.pop(index_to_delete)

    def delete_all(self):
        self.__items.clear()

    def find(self) -> List[Product]:
        return copy.deepcopy(self.__items)
