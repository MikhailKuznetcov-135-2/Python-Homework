from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver, wait_timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")

    def open(self, url: str) -> None:
        self.driver.get(url)

    def set_delay(self, value: int) -> None:
        element = self.wait.until(
            EC.visibility_of_element_located(self.delay_input)
        )
        element.clear()
        element.send_keys(str(value))

    def click_button(self, text: str) -> None:
        locator = (By.XPATH, f"//span[text()='{text}']")
        btn = self.wait.until(EC.element_to_be_clickable(locator))
        btn.click()

    def get_result(self) -> str:
        element = self.wait.until(
            EC.visibility_of_element_located(self.result_field)
        )
        return element.text.strip()