import allure


@allure.suite(suite_name='Тесты Yandex для Jenkins')
class TestYandex:
    @allure.title('Открытие поисковой строки')
    @allure.description('Открытие поисковой строки')
    def test_yandex(self, driver):
        driver.open_base_page()

