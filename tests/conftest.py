import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    browser_config.base_url = 'https://demoqa.com'
    browser.config.window_width = 700
    browser.config.window_height = 1900
    yield
    browser.quit()
