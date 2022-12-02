import allure


@allure.suite(suite_name='Тесты для Jenkins')
class TestJenkins:
    @allure.title('First test')
    @allure.description('First test')
    def test_first(self):
        with allure.step('Ассерт'):
            assert 1 == 1, "Ошибка"

    @allure.description('Second test')
    def test_second(self):
        with allure.step('Second test'):
            assert 2 == 2, "Ошибка"