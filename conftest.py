import pytest
from selene import browser


@pytest.fixture()
def setting_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 720
    yield
    browser.quit()
