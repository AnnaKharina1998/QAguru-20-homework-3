import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_options():
    browser.config.window_width = '1600'
    browser.config.window_height = '900'

    yield
    browser.quit()


















