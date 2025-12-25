from ..pages.dashboard_page import DashboardPage
from ..pages.login_page import LoginPage


class DeviceWeb:
    def __init__(self, page, base_url):
        self._page = page
        self._base_url = base_url

    def open_login(self):
        return LoginPage(self._page, self._base_url).open()

    def login(self, username, password):
        return LoginPage(self._page, self._base_url).open().login(username, password)

    def dashboard(self):
        return DashboardPage(self._page, self._base_url)
