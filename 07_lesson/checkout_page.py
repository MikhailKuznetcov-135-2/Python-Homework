from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver, wait_timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.CSS_SELECTOR, "input.cart_button")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        fn_el = self.wait.until(
            EC.visibility_of_element_located(self.first_name_input)
        )
        ln_el = self.wait.until(
            EC.visibility_of_element_located(self.last_name_input)
        )
        pc_el = self.wait.until(
            EC.visibility_of_element_located(self.postal_code_input)
        )

        fn_el.clear()
        fn_el.send_keys(first_name)
        ln_el.clear()
        ln_el.send_keys(last_name)
        pc_el.clear()
        pc_el.send_keys(postal_code)

        btn = self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        )
        btn.click()

    def get_total(self) -> float:
        label_el = self.wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        text = label_el.text.strip()
        value_str = text.replace("Total: ", "").replace("$", "")
        return float(value_str)