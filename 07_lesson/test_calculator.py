import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


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
    assert result == "15"
