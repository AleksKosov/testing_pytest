import allure


@allure.description('Тестирование Яндекса')
def test_yandex():
    with allure.step('Ассерт'):
        assert 1 == 1, "Ошибка"

