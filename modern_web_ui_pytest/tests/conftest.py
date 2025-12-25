import pytest

from framework.core.browser import BrowserManager
from framework.core.config import settings
from framework.device.device_web import DeviceWeb


@pytest.fixture(scope="session")
def browser():
    manager = BrowserManager()
    browser = manager.start()
    yield browser
    manager.stop()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture
def device_web(page):
    return DeviceWeb(page, settings.base_url)
