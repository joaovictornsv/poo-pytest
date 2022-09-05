import copy
from src.app.exceptions import NotFoundException
from src.app.constants import CartErrorMessages
from .product import Product


class Cart:
    def __init__(self):
        self.__items = []

    def add_product(self, product: Product) -> None:
        self.__items.append(product)

    def remove_product(self, product_id: str) -> None:
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

    def calculate_price(self) -> int:
        total = 0

        for product in self.__items:
            total += product.price

        return total

    def total_itens(self) -> int:
        return len(self.__items)

    def empty_cart(self) -> None:
        self.__items = []

    def get_items(self):
        return copy.deepcopy(self.__items)
