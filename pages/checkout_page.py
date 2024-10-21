from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators for checkout items
        self.address_details_heading = page.locator('.step-one .heading', has_text="Address Details")
        self.review_order_heading = page.locator('.step-one .heading', has_text="Review Your Order")
        self.order_comment_textarea = page.locator('#ordermsg textarea')
        self.place_order_button = page.locator('a.btn.btn-default.check_out')
        self.register_login_button = self.page.locator('a[href="/login"]', has_text="Register / Login")
        self.delivery_address_section = page.locator('ul#address_delivery')
        self.billing_address_section = page.locator('ul#address_invoice')

    # Method to verify address details section is visible
    def verify_address_details(self):
        expect(self.address_details_heading).to_be_visible()

    # Method to verify review order section is visible
    def verify_review_order(self):
        expect(self.review_order_heading).to_be_visible()

    # Method to add a comment about the order
    def add_order_comment(self, comment: str):
        self.order_comment_textarea.fill(comment)

    # Method to click the 'Place Order' button
    def click_place_order_button(self):
        self.place_order_button.click()

    def click_register_login_button(self):
        self.register_login_button.click()

     # Method to verify that delivery and billing address match the registration address
    def verify_address_details_match_registration(self, address_details: dict):
        for key, value in address_details.items():
            expect(self.delivery_address_section).to_contain_text(value)
            expect(self.billing_address_section).to_contain_text(value)