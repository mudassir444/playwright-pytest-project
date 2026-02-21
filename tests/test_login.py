import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:

    def test_successful_login(self, page):
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")
        inventory = InventoryPage(page)
        assert inventory.is_inventory_displayed(), "Inventory list should be visible after login"

    def test_failed_login_wrong_password(self, page):
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "wrong_password")
        error = login.get_error_message()
        assert error is not None and len(error) > 0
        assert "Epic sadface" in error or "Username and password do not match" in error

    @pytest.mark.parametrize("username,password,expected_error_fragment", [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("locked_out_user", "secret_sauce", "locked out"),
    ])
    def test_invalid_logins(self, page, username, password, expected_error_fragment):
        login = LoginPage(page)
        login.navigate()
        login.login(username, password)
        error = login.get_error_message()
        assert error is not None
        assert expected_error_fragment.lower() in error.lower(), \
            f"Expected '{expected_error_fragment}' in error: '{error}'"
