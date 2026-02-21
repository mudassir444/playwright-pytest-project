import pytest
from playwright.sync_api import Page, expect

def test_saucedemo_login(page: Page):
    # Navigate to the site
    page.goto("https://www.saucedemo.com/")
    
    # Perform login
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # Verify we logged in successfully
    expect(page.locator(".title")).to_have_text("Products")
