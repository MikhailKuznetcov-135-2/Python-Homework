from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        # 1. Откройте страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Найдите и нажмите на кнопку "Start"
        start_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.example button"))
        )
        start_button.click()

        # 3. Дождитесь появления текста "Hello World!"
        hello_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish"))
        )

        # 4. Сделайте скриншот страницы
        driver.save_screenshot("test_lesson06_task1_screenshot.png")

        # 5. Проверьте, что появившийся текст равен "Hello World!"
        assert hello_element.text == "Hello World!", "Текст не совпадает с ожидаемым"
    finally:
        driver.quit()
        