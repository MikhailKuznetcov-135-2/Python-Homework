from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver, wait_timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")

    def open_cart(self) -> None:
        link = self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        )
        link.click()

    def go_to_checkout(self) -> None:
        btn = self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        btn.click()
        