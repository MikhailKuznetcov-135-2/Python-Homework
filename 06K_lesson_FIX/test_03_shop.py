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

def test_checkout_total(driver):
    base_url = "https://www.saucedemo.com/"
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)
    user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    pass_input = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    user_input.send_keys("standard_user")
    pass_input.send_keys("secret_sauce")
    login_btn.click()
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item_name in items_to_add:
        xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        add_btn.click()
    cart_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_link.click()
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()
    first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    last_name = driver.find_element(By.ID, "last-name")
    postal = driver.find_element(By.ID, "postal-code")
    first_name.send_keys("Иван")
    last_name.send_keys("Петров")
    postal.send_keys("123456")
    continue_btn = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    continue_btn.click()
    total_el = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
