import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    #browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 800
    browser.config.window_height = 1000
    yield
    browser.quit()
