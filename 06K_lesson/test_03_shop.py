import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(GeckoDriverManager().install(), options=options)
    yield driver
    driver.quit()

def test_checkout_total(driver):
    base_url = "https://www.saucedemo.com/"
    driver.get(base_url)

    wait = WebDriverWait(driver, 10)

    # Авторизация
    user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    pass_input = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.CLASS_NAME, "login_button")

    user_input.send_keys("standard_user")
    pass_input.send_keys("secret_sauce")
    login_btn.click()

    # Добавляем товары в корзину
    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]

    for product_name in products_to_add:
        # Ищем карточку товара по названию
        product_card = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[contains(@class, 'inventory_item') and .//*[text()='{product_name}']]")
            )
        )
        add_btn = product_card.find_element(By.CSS_SELECTOR, ".btn_primary")
        add_btn.click()

    # Переход в корзину
    cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_container")))
    cart_link.click()

    checkout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout_button")))
    checkout_btn.click()

    # Заполнение формы
    first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    last_name = driver.find_element(By.ID, "last-name")
    postal = driver.find_element(By.ID, "postal-code")

    first_name.send_keys("Ivan")
    last_name.send_keys("Petrov")
    postal.send_keys("12345")

    continue_btn = driver.find_element(By.CSS_SELECTOR, ".cart_button")
    continue_btn.click()

    # Проверка итоговой суммы
    total_el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_line")))
    total_text = total_el.text  # обычно: "Total: $58.29"

    # Парсим сумму
    import re
    match = re.search(r"\$([\d.]+)", total_text)
    assert match, f"Could not parse total amount from '{total_text}'"
    total_value = float(match.group(1))

    expected_total = 58.29
    assert total_value == expected_total, f"Expected total ${expected_total}, got ${total_value}"