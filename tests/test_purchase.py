from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestPurchase:

    def test_complete_purchase(self, logged_in_page):
        page = logged_in_page
        inventory = InventoryPage(page)
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()
        cart = CartPage(page)
        assert cart.get_cart_items_count() == 1
        assert cart.is_item_in_cart("Sauce Labs Backpack")
        cart.checkout()
        checkout = CheckoutPage(page)
        checkout.fill_info("Test", "User", "12345")
        checkout.continue_to_overview()
        checkout.finish()
        success = checkout.get_success_message()
        assert "Thank you for your order!" in success

    def test_cart_is_empty_initially(self, logged_in_page):
        page = logged_in_page
        page.goto("https://www.saucedemo.com/cart.html")
        cart = CartPage(page)
        assert cart.get_cart_items_count() == 0
