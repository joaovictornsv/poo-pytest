from typing import List, Type
from src.app.repositories import ProductRepository
from src.app.entities import Product


class Cart:
    def __init__(self, product_repository: Type[ProductRepository]):
        self.__product_repository = product_repository

    def add_product(self, product: Product) -> None:
        self.__product_repository.create(product)

    def remove_product(self, product_id: str) -> None:
        self.__product_repository.delete(product_id)

    def calculate_price(self) -> float:
        itens = self.__product_repository.find()
        total = 0

        for product in itens:
            total += product.price

        return total

    def total_itens(self) -> int:
        itens = self.__product_repository.find()
        return len(itens)

    def empty_cart(self) -> None:
        self.__product_repository.delete_all()

    def get_items(self) -> List[Product]:
        itens = self.__product_repository.find()
        return itens
