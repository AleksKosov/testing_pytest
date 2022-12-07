import pytest
import json
from webdriver.webdriver import BasePage


@pytest.fixture(scope='session')
def config():
    with open('./config.json', 'r', encoding='utf-8') as data:
        data = json.loads(data.read())
        return data


@pytest.fixture(scope='session')
def driver(request, config):
    selenoid = request.config.getoption("--selenoid")
    driver = BasePage(host=config['host'],
                      url=config['base_url'],
                      capabilities=config['capabilities'],
                      selenoid=selenoid)
    yield driver
    request.addfinalizer(driver.quit)


def pytest_addoption(parser):
    parser.addoption("--selenoid", action="store_true", default=False)
