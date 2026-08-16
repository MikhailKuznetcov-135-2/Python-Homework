import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()

def test_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 30)
    
    el = wait.until(EC.visibility_of_element_located((By.NAME, "first-name")))
    el.clear()
    el.send_keys("Иван")
    
    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='submit']")))
    submit_btn.click()
    
    zip_code = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    assert "is-invalid" in zip_code.get_attribute("class")