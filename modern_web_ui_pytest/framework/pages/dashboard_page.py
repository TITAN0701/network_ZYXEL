from ..core.base_page import BasePage


class DashboardPage(BasePage):
    def open(self):
        self.page.goto(f"{self.base_url}/")
        return self

    def assert_logged_in(self, username):
        header = self.page.locator("h2")
        header.wait_for()
        assert header.inner_text().strip() == "Secure Area"
        flash = self.page.locator("#flash")
        flash.wait_for()
        assert "You logged into a secure area!" in flash.inner_text()

    def assert_secure_area(self):
        self.assert_logged_in("")
