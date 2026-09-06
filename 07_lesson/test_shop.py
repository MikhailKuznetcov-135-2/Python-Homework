import pytest
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver_firefox():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.feature("Shop")
@allure.story("Оформление заказа и проверка итоговой суммы")
@allure.title("Проверка итоговой суммы чека")
@allure.description(
    "Добавляет товары в корзину, оформляет заказ и проверяет, что итоговая сумма равна 58.29."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_checkout_total(driver_firefox):
    login_page = LoginPage(driver_firefox)
    inventory_page = InventoryPage(driver_firefox)
    cart_page = CartPage(driver_firefox)
    checkout_page = CheckoutPage(driver_firefox)

    base_url = "https://www.saucedemo.com/"

    with allure.step("Войти в магазин как стандартный пользователь"):
        login_page.open(base_url)
        login_page.login("standard_user", "secret_sauce")

    items = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie",
    ]

    with allure.step("Добавить товары в корзину"):
        for product_id in items:
            inventory_page.add_to_cart(product_id)

    with allure.step("Перейти в корзину и начать оформление заказа"):
        cart_page.open_cart()
        cart_page.go_to_checkout()

    with allure.step("Заполнить форму оформления заказа"):
        checkout_page.fill_checkout_form("Ivan", "Ivanov", "12345")

    total = checkout_page.get_total()
    expected_total = 58.29

    with allure.step(f"Проверить, что итоговая сумма {total} равна ожидаемой {expected_total}"):
        assert total == expected_total, f"Ожидалась сумма {expected_total}, получена {total}"