from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, wait_timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self, url: str):
        self.driver.get(url)

    def login(self, username: str, password: str):
        user_el = self.wait.until(EC.visibility_of_element_located(self.username_input))
        pass_el = self.wait.until(EC.visibility_of_element_located(self.password_input))
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_button))

        user_el.clear()
        user_el.send_keys(username)
        pass_el.clear()
        pass_el.send_keys(password)
        login_btn.click()