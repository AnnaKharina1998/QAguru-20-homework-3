import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_options():
    browser.config.window_width = '1600'
    browser.config.window_height = '900'

    yield
    browser.quit()

@pytest.fixture(scope="function", autouse=False)
def google():
    browser.config.base_url = 'https://google.com/'

@pytest.fixture(scope="function", autouse=False)
def yandex():
    browser.config.base_url = 'https://ya.ru/'

@pytest.fixture(scope="function", autouse=False)
def duck():
    browser.config.base_url = 'https://duckduckgo.com/'

















