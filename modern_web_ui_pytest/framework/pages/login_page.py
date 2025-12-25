from ..core.base_page import BasePage


class LoginPage(BasePage):
    def open(self):
        self.page.goto(f"{self.base_url}/login")
        return self

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click('button[type="submit"]')
        return self

    def assert_error(self, message):
        error = self.page.locator("#flash")
        error.wait_for()
        assert message in error.inner_text()
