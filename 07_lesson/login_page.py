from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    """Страница входа в магазин."""

    def __init__(self, driver, wait_timeout: int = 10) -> None:
        """
        :param driver: экземпляр WebDriver
        :param wait_timeout: время ожидания элементов
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу входа по URL {url}")
    def open(self, url: str) -> None:
        """
        :param url: URL страницы входа
        :return: None
        """
        self.driver.get(url)

    @allure.step("Выполнить вход с логином '{username}' и паролем '{password}'")
    def login(self, username: str, password: str) -> None:
        """
        Заполняет поля и нажимает кнопку входа.
        :param username: логин пользователя
        :param password: пароль пользователя
        :return: None
        """
        user_el = self.wait.until(
            EC.visibility_of_element_located(self.username_input)
        )
        pass_el = self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        )
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        )

        user_el.clear()
        user_el.send_keys(username)
        pass_el.clear()
        pass_el.send_keys(password)
        login_btn.click()
