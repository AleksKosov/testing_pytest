import time

import allure
from selenium import webdriver


@allure.suite(suite_name='Тесты Yandex для Jenkins')
class TestYandex:
    @allure.title('Открытие поисковой строки')
    @allure.description('Открытие поисковой строки')
    def test_yandex(self):
        with allure.step('Открытие поисковой строки'):
            driver = None
            try:
                capabilities = {
                    "browserName": "firefox",
                    "browserVersion": "106.0",
                    "selenoid:options": {
                        "enableVNC": True,
                        "enableVideo": False
                    }
                }
                driver = webdriver.Remote(
                    command_executor="http://localhost:4444//wd/hub",
                    desired_capabilities=capabilities
                )
                driver.get('https://ya.ru')
            finally:
                driver.quit()

