import time

import allure
from selenium import webdriver


@allure.suite(suite_name='Тесты для Jenkins')
class TestJenkins:
    @allure.title('First test')
    @allure.description('First test')
    def test_yandex(self):
        with allure.step('Ассерт'):
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

