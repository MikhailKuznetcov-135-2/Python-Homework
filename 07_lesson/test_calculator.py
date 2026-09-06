import pytest
import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.feature("Calculator")
@allure.story("Проверка сложения на медленном калькуляторе")
@allure.title("Тест сложения 7 + 8")
@allure.description("Проверяет, что калькулятор корректно складывает 7 и 8 при задержке 45 секунд.")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator_addition(driver):
    page = CalculatorPage(driver)
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    page.open(url)
    page.set_delay(45)

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result("15")
    assert result == "15", f"Ожидалось 15, получено {result}"