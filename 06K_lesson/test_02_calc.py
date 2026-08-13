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

def test_slow_calculator(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)

    wait = WebDriverWait(driver, 60)  # увеличиваем таймаут, т.к. ждём 45 сек

    delay_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    def click_btn(text):
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[normalize-space()='{text}']")))
        btn.click()

    click_btn("7")
    click_btn("+")
    click_btn("8")
    click_btn("=")

    result_el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".result")))
    # В зависимости от страницы результат может быть в .result или в input
    # Если это input, то берём .get_attribute("value")
    result_text = result_el.text.strip() if result_el.tag_name != "input" else result_el.get_attribute("value").strip()

    assert result_text == "15", f"Expected 15, got {result_text}"