from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Замените на реальные значения из браузера
USER_1_COOKIE = {"name": "sessionid", "value": "ВАШ_COOKIE_ДЛЯ_ПОЛЬЗОВАТЕЛЯ_1"}
USER_2_COOKIE = {"name": "sessionid", "value": "ВАШ_COOKIE_ДЛЯ_ПОЛЬЗОВАТЕЛЯ_2"}

# URL профилей пользователей Gitflic — подставьте реальные URL ваших аккаунтов
USER_1_PROFILE_URL = "https://gitflic.ru/user/username1"
USER_2_PROFILE_URL = "https://gitflic.ru/user/username2"


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Откройте главную страницу
        driver.get("https://gitflic.ru/")

        # --- Пользователь 1 ---
        # Установите cookie пользователя 1
        driver.add_cookie(USER_1_COOKIE)

        # Обновите страницу, чтобы cookie применились
        driver.refresh()

        # Перейдите на страницу пользователя 1
        driver.get(USER_1_PROFILE_URL)

        # Сохраните текущий URL
        url_user_1 = driver.current_url

        # Разлогиньтесь (очистите куки)
        driver.delete_all_cookies()

        # --- Пользователь 2 ---
        # Установите cookie пользователя 2
        driver.add_cookie(USER_2_COOKIE)

        # Обновите страницу
        driver.refresh()

        # Перейдите на страницу пользователя 2
        driver.get(USER_2_PROFILE_URL)

        # Сохраните текущий URL
        url_user_2 = driver.current_url

        # Проверьте, что URL для пользователя 1 и пользователя 2 различаются
        assert url_user_1 != url_user_2, "URL профилей пользователей совпадают"
    finally:
        driver.quit()
        