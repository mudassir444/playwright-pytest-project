from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_list = page.locator(".inventory_list")
        self.add_backpack_btn = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_backpack_to_cart(self):
        self.add_backpack_btn.click()
        return self

    def go_to_cart(self):
        self.cart_icon.click()
        return self

    def is_inventory_displayed(self):
        return self.inventory_list.is_visible()
