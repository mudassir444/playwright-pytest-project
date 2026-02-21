from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator("#first-name")
        self.last_name_field = page.locator("#last-name")
        self.postal_code_field = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.success_message = page.locator(".complete-header")

    def fill_info(self, first: str, last: str, zip: str):
        self.first_name_field.fill(first)
        self.last_name_field.fill(last)
        self.postal_code_field.fill(zip)
        return self

    def continue_to_overview(self):
        self.continue_button.click()
        return self

    def finish(self):
        self.finish_button.click()
        return self

    def get_success_message(self):
        return self.success_message.text_content()
