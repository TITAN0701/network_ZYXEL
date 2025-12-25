from pytest_bdd import given, when, then, scenarios
from framework.core.config import settings

scenarios("../features/login.feature")


@given("user opens login page")
def open_login(device_web):
    device_web.open_login()


@when("user logs in with valid credentials")
def do_login(device_web):
    device_web.login(settings.login_username, settings.login_password)


@then("user should see the secure area")
def assert_secure(device_web):
    device_web.dashboard().assert_secure_area()
