from playwright.sync_api import Page, expect

class PaymentPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators for payment details
        self.name_on_card = page.locator('[data-qa="name-on-card"]')
        self.card_number = page.locator('[data-qa="card-number"]')
        self.cvc = page.locator('[data-qa="cvc"]')
        self.expiry_month = page.locator('[data-qa="expiry-month"]')
        self.expiry_year = page.locator('[data-qa="expiry-year"]')
        self.pay_and_confirm_order_button = page.locator('[data-qa="pay-button"]')
        self.order_success_message = page.locator('#success_message .alert-success')

    # Method to enter payment details
    def enter_payment_details(self, name: str, card_number: str, cvc: str, expiry_month: str, expiry_year: str):
        self.name_on_card.fill(name)
        self.card_number.fill(card_number)
        self.cvc.fill(cvc)
        self.expiry_month.fill(expiry_month)
        self.expiry_year.fill(expiry_year)

    # Method to click the 'Pay and Confirm Order' button
    def click_pay_and_confirm_order(self):
        self.pay_and_confirm_order_button.click()

    # Method to verify order success message
    def verify_order_success_message(self):
        expect(self.order_success_message).to_have_text('Your order has been placed successfully!')
