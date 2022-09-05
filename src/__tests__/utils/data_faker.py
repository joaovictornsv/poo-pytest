import random
from faker import Faker

faker = Faker()

class DataFaker:
    def float_number(self):
        return float(f"{random.random() * 10:.2f}")

    def name(self):
        return faker.name()
