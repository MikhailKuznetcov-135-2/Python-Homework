import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver_firefox():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_shop_checkout_total(driver_firefox):
    login_page = LoginPage(driver_firefox)
    inventory_page = InventoryPage(driver_firefox)
    cart_page = CartPage(driver_firefox)
    checkout_page = CheckoutPage(driver_firefox)

    base_url = "https://www.saucedemo.com/"
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")

    items = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie",
    ]

    for product_id in items:
        inventory_page.add_to_cart(product_id)

    cart_page.go_to_checkout()
    checkout_page.fill_checkout_form("Ivan", "Ivanov", "12345")

    total = checkout_page.get_total()
    expected_total = 58.29
    assert total == expected_total
    