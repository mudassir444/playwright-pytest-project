import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def logged_in_page(login_page):
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    return login_page.page
