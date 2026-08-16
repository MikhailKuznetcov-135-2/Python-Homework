import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeDriverManager


@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(EdgeDriverManager().install(), options=options)
    yield driver
    driver.quit()


def test_form_validation(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for field_id, value in fields.items():
        el = wait.until(EC.visibility_of_element_located((By.NAME, field_id)))
        el.clear()
        el.send_keys(value)

    submit_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='submit']"))
    )
    submit_btn.click()

    zip_code = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "is-invalid" in zip_code.get_attribute("class"), (
        f"Zip code should be invalid, got classes: {zip_code.get_attribute('class')}"
    )

    for field_id in fields.keys():
        field = wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        assert "is-valid" in field.get_attribute("class"), (
            f"Field {field_id} should be valid, got classes: {field.get_attribute('class')}"
        )