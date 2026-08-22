from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver, wait_timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)

    def add_item_by_name(self, item_name: str):
        """
        item_name — точное название товара, как на странице.
        На saucedemo кнопка добавления имеет data-testid, но можно искать по названию товара.
        Здесь используем XPath по тексту товара и кнопку рядом.
        """
        # Ищем карточку товара по названию и затем кнопку «Add to cart» внутри неё
        locator = (
            By.XPATH,
            f"//div[contains(@class, 'inventory_item')]//div[@class='inventory_item_name' and normalize-space()='{item_name}']/parent::div//button"
        )
        btn = self.wait.until(EC.element_to_be_clickable(locator))
        btn.click()