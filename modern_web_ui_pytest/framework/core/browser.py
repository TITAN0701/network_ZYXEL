from playwright.sync_api import sync_playwright

from .config import settings


class BrowserManager:
    def __init__(self):
        self._playwright = None
        self._browser = None

    def start(self):
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(
            headless=settings.headless,
            slow_mo=settings.slowmo_ms,
        )
        return self._browser

    def stop(self):
        if self._browser:
            self._browser.close()
            self._browser = None
        if self._playwright:
            self._playwright.stop()
            self._playwright = None
