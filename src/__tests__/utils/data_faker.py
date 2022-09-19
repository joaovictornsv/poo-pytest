import random
from faker import Faker
from src.app.entities import Product

faker = Faker()


class DataFaker:
    def float_number(self) -> float:
        return float(f"{random.random() * 10 + 1:.2f}")

    def name(self) -> str:
        return faker.name()

    def product(self) -> Product:
        return Product(self.name(), self.float_number())
