from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """Страница калькулятора с медленными вычислениями."""

    def __init__(self, driver, wait_timeout: int = 60) -> None:
        """
        :param driver: экземпляр WebDriver
        :param wait_timeout: время ожидания элементов в секундах
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу калькулятора по URL {url}")
    def open(self, url: str) -> None:
        """
        Открывает страницу по указанному URL.
        :param url: адрес страницы
        :return: None
        """
        self.driver.get(url)

    @allure.step("Установить задержку {value} секунд")
    def set_delay(self, value: int) -> None:
        """
        Устанавливает задержку для медленных вычислений.
        :param value: значение задержки в секундах
        :return: None
        """
        element = self.wait.until(
            EC.visibility_of_element_located(self.delay_input)
        )
        element.clear()
        element.send_keys(str(value))

    @allure.step("Нажать кнопку с текстом '{text}'")
    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку по тексту внутри неё.
        :param text: текст кнопки
        :return: None
        """
        locator = (By.XPATH, f"//span[text()='{text}']")
        btn = self.wait.until(EC.element_to_be_clickable(locator))
        btn.click()

    @allure.step("Получить результат и проверить, что он содержит '{expected}'")
    def get_result(self, expected: str) -> str:
        """
        Ждёт появления ожидаемого текста в поле результата и возвращает его.
        :param expected: ожидаемая подстрока результата
        :return: текст результата из поля
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.result_field, expected)
        )
        return self.driver.find_element(*self.result_field).text.strip()
    