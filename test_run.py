import allure


@allure.title('First test')
@allure.description('First test')
def test_first():
    with allure.step('Ассерт'):
        assert 1 == 1, "Ошибка"


@allure.description('Second test')
def test_second():
    with allure.step('Second test'):
        assert 2 == 2, "Ошибка"