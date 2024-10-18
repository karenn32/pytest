from playwright.sync_api import Page, expect
import os

class PaymentDonePage:
    def __init__(self, page: Page):
        self.page = page
        # Locator for the order confirmation message
        self.order_confirmation_message = page.locator('p', has_text="Congratulations! Your order has been confirmed!")
        self.order_placed_heading = page.locator('h2[data-qa="order-placed"]')
        self.download_invoice_button = page.locator('a[href*="/download_invoice"]')
        self.continue_button = page.locator('a[data-qa="continue-button"]')

    # Method to verify the order confirmation message is visible and has correct content
    def verify_order_confirmation_message(self):
        expect(self.order_confirmation_message).to_be_visible()
        expect(self.order_confirmation_message).to_have_text("Congratulations! Your order has been confirmed!")

    # Method to verify the 'Order Placed!' heading is visible
    def verify_order_placed_heading(self):
        expect(self.order_placed_heading).to_be_visible()
        expect(self.order_placed_heading).to_have_text("Order Placed!")

  # Method to click the "Download Invoice" button
    def download_invoice(self):
        with self.page.expect_download() as download_info:
    # Perform the action that initiates download
            self.download_invoice_button.click()
        download = download_info.value
        download_path = os.path.join(os.getcwd(), 'invoice.txt')
        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(download_path)
        print(f"Invoice downloaded and saved as {download_path}")


    # Method to click the "Continue" button after downloading the invoice
    def click_continue_button(self):
        self.continue_button.click()