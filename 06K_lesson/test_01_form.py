import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.safari import SafariDriverManager
import platform

@pytest.fixture
def driver():
    system = platform.system()
    if system == "Windows":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(EdgeDriverManager().install(), options=options)
    elif system == "Darwin":
        # Safari на macOS не поддерживает webdriver-manager напрямую:
        # для Safari нужно включить "Allow Remote Automation" в Safari и использовать системный драйвер
        options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=options)
    else:
        raise RuntimeError("Unsupported OS for this task")
    yield driver
    driver.quit()

def test_form_validation(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    # Заполняем поля
    fields = {
        "fname": "Иван",
        "lname": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone": "+7985899998787",
        "zip": "",  # оставляем пустым
        "city": "Москва",
        "country": "Россия",
        "position": "QA",
        "company": "SkyPro",
    }

    for name, value in fields.items():
        el = wait.until(EC.visibility_of_element_located((By.NAME, name)))
        if value:
            el.clear()
            el.send_keys(value)

    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))
    submit_btn.click()

    # Ожидаем появления валидации
    zip_el = wait.until(EC.presence_of_element_located((By.NAME, "zip")))
    other_fields = [
        wait.until(EC.presence_of_element_located((By.NAME, k)))
        for k in ["fname", "lname", "address", "email", "phone", "city", "country", "position", "company"]
    ]

    # Проверяем цвет полей (через CSS color / border-color — зависит от реализации валидации на странице)
    # На этой странице валидация обычно выражается через border-color.
    zip_color = zip_el.value_of_css_property("border-color")
    assert "red" in zip_color.lower(), f"Zip code should be highlighted red, got {zip_color}"

    for el in other_fields:
        color = el.value_of_css_property("border-color")
        assert "green" in color.lower(), f"Field should be highlighted green, got {color}"