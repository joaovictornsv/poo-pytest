from src.app.entities import Product


def test_product_name_and_price():
    name = "Product Example"
    price = 1.99
    product = Product(name, price)
    assert product.name == name
    assert product.price == price
