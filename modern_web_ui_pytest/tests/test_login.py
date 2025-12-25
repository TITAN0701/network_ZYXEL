from framework.core.config import settings


def test_login_success(device_web):
    device_web.login(settings.login_username, settings.login_password)
    device_web.dashboard().assert_logged_in(settings.login_username)


def test_login_failure(device_web):
    login_page = device_web.open_login()
    login_page.login(settings.invalid_username, settings.invalid_password)
    login_page.assert_error(settings.login_error_message)
