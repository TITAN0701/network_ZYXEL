from framework.core.config import settings


def test_home_title(page):
    page.goto(f"{settings.base_url}/")
    assert page.title() != ""
