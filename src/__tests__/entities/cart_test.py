import pytest
from src.app.entities import Product, Cart
from src.app.exceptions import NotFoundException
from src.app.constants import CartErrorMessages, HttpStatusCode
from src.__tests__.utils import DataFaker

faker = DataFaker()


def test_cart_add_product():
    cart = Cart()

    # Create product
    p_name = faker.name()
    p_price = faker.float_number()
    p_ = Product(p_name, p_price)

    cart.add_product(p_)

    assert cart.total_itens() == 1
    assert cart.calculate_price() == p_price


def test_cart_remove_product():
    cart = Cart()

    # Create product
    p_name = faker.name()
    p_price = faker.float_number()
    p_ = Product(p_name, p_price)

    cart.add_product(p_)
    cart.remove_product(p_.id)

    assert cart.total_itens() == 0
    assert cart.calculate_price() == 0


def test_cart_remove_product_but_not_exists():
    cart = Cart()

    # Create product
    p_name = faker.name()
    p_price = faker.float_number()
    p_ = Product(p_name, p_price)

    cart.add_product(p_)

    with pytest.raises(NotFoundException) as error:
        cart.remove_product("1")

    assert error.value.message == CartErrorMessages.PRODUCT_NOT_FOUND.value
    assert error.value.code == HttpStatusCode.NOT_FOUND.value
    assert cart.total_itens() == 1
    assert cart.calculate_price() == p_price


def test_cart_calculate_price():
    cart = Cart()

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

    assert cart.total_itens() == 2
    assert cart.calculate_price() == p1_price + p2_price


def test_cart_empty_cart():
    cart = Cart()

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

    cart.empty_cart()
    assert cart.total_itens() == 0


def test_cart_total_items():
    cart = Cart()
    assert cart.total_itens() == 0


def test_cart_get_items():
    cart = Cart()
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
