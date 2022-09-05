import pytest
from src.app.entities import Product
from src.app.business import Cart
from src.app.exceptions import NotFoundException
from src.app.constants import CartErrorMessages, HttpStatusCode
from src.app.repositories import ProductRepository
from src.__tests__.utils import DataFaker
from unittest.mock import Mock

faker = DataFaker()


def test_cart_add_product():
    # Setup
    product_repository = ProductRepository()
    cart = Cart(product_repository)

    # Create product
    pdt = faker.product()

    # Mock
    product_repository.find = Mock(return_value=[pdt])

    assert cart.total_itens() == 1
    assert cart.calculate_price() == pdt.price


def test_cart_remove_product():
    product_repository = ProductRepository()
    cart = Cart(product_repository)

    # Create product
    pdt_name = faker.name()
    pdt_price = faker.float_number()
    pdt = Product(pdt_name, pdt_price)

    cart.add_product(pdt)
    cart.remove_product(pdt.id)

    assert cart.total_itens() == 0
    assert cart.calculate_price() == 0


def test_cart_remove_product_but_not_exists():
    product_repository = ProductRepository()
    cart = Cart(product_repository)

    # Create product
    pdt_name = faker.name()
    pdt_price = faker.float_number()
    pdt = Product(pdt_name, pdt_price)

    cart.add_product(pdt)

    with pytest.raises(NotFoundException) as error:
        cart.remove_product("1")

    assert error.value.message == CartErrorMessages.PRODUCT_NOT_FOUND.value
    assert error.value.code == HttpStatusCode.NOT_FOUND.value
    assert cart.total_itens() == 1
    assert cart.calculate_price() == pdt_price


def test_cart_calculate_price():
    product_repository = ProductRepository()
    cart = Cart(product_repository)

    # Create product 1
    p1_price = faker.float_number()
    p1_ = Product(faker.name(), p1_price)

    # Create product 2
    p2_price = faker.float_number()
    p2_ = Product(faker.name(), p2_price)

    product_repository.find = Mock(return_value=[p1_, p2_])
    assert cart.total_itens() == 2
    assert cart.calculate_price() == p1_price + p2_price


def test_cart_empty_cart():
    product_repository = ProductRepository()
    cart = Cart(product_repository)

    # Insert products
    cart.add_product(faker.product())
    cart.add_product(faker.product())

    cart.empty_cart()
    assert cart.total_itens() == 0


def test_cart_total_items():
    product_repository = ProductRepository()
    cart = Cart(product_repository)

    # Create product 1
    p1_ = Product(faker.name(), faker.float_number())

    # Mock
    product_repository.find = Mock(return_value=[p1_])

    assert cart.total_itens() == 1


def test_cart_get_items():
    product_repository = ProductRepository()
    cart = Cart(product_repository)
    # Create product 1
    p1_name = faker.name()
    p1_price = faker.float_number()
    p1_ = Product(p1_name, p1_price)

    # Create product 2
    p2_name = faker.name()
    p2_price = faker.float_number()
    p2_ = Product(p2_name, p2_price)

    # Insert products
    cart.add_product(p1_)
    cart.add_product(p2_)
    itens = cart.get_items()
    assert len(itens) == cart.total_itens()
