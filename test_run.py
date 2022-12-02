import allure


@allure.description('Тестирование Яндекса')
def test_yandex():
    with allure.step('Ассерт'):
        assert 2 == 1, "Ошибка"

