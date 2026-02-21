from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("#checkout")

    def get_cart_items_count(self):
        return self.cart_items.count()

    def is_item_in_cart(self, item_name: str):
        items = self.item_names.all_text_contents()
        return item_name in items

    def checkout(self):
        self.checkout_button.click()
        return self
