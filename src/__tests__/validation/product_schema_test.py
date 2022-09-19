import pytest
from src.app.entities import Product
from src.app.exceptions import BadRequestException
from src.app.constants import HttpStatusCode


def test_product_valid():
    valid_name = "Product"
    valid_price = 2
    pdt = Product(valid_name, valid_price)

    assert pdt.name == valid_name
    assert pdt.price == valid_price


def test_product_invalid_name():
    invalid_name = "Pr"
    valid_price = 2

    # Create product
    with pytest.raises(BadRequestException) as error:
        Product(invalid_name, valid_price)

    assert error.value.message == 'Invalid field "name": Shorter than minimum length 3'
    assert error.value.code == HttpStatusCode.BAD_REQUEST.value


def test_product_invalid_price():
    valid_name = "Product"
    invalid_price = 200

    # Create product
    with pytest.raises(BadRequestException) as error:
        Product(valid_name, invalid_price)

    assert (
        error.value.message
        == 'Invalid field "price": 200.0 is greater than maximum value 100'
    )
    assert error.value.code == HttpStatusCode.BAD_REQUEST.value
