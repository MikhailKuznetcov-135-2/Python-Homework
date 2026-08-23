from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id: str) -> "InventoryPage":
        btn_id = f"add-to-cart-{product_id}"
        btn = self.driver.find_element(By.ID, btn_id)
        btn.click()
        return self
    