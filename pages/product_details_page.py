from playwright.sync_api import Page, expect

class ProductDetailsPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.product_name = page.locator('.product-information h2')
        self.product_category = page.locator('.product-information p', has_text="Category")
        self.product_price = page.locator('.product-information span span')
        self.product_availability = page.locator('.product-information p', has_text="Availability")
        self.product_condition = page.locator('.product-information p', has_text="Condition")
        self.product_brand = page.locator('.product-information p', has_text="Brand")
        self.quantity_input = page.locator('input#quantity')
        self.add_to_cart_button = page.locator('.btn.btn-default.cart')
        self.view_cart_button = page.locator('a[href="/view_cart"]', has_text="View cart")
        self.review_section_title = page.locator('a', has_text="Write Your Review")
        self.review_name_input = page.locator('input[id="name"]')
        self.review_email_input = page.locator('input[id="email"]')
        self.review_textarea = page.locator('textarea[id="review"]')
        self.submit_review_button = page.locator('button[id="button-review"]')
        self.success_message = page.locator('.alert-success.alert', has_text='Thank you for your review.')
        
    # Method to verify the product details
    def verify_product_details(self, name: str, category: str, price: str, availability: str, condition: str, brand: str):
        expect(self.product_name).to_have_text(name)
        expect(self.product_category).to_have_text(f"Category: {category}")
        expect(self.product_price).to_have_text(price)
        expect(self.product_availability).to_have_text(f"Availability: {availability}")
        expect(self.product_condition).to_have_text(f"Condition: {condition}")
        expect(self.product_brand).to_have_text(f"Brand: {brand}")

    def set_product_quantity(self, quantity: int):
        self.quantity_input.fill(str(quantity))

    def click_add_to_cart_button(self):
        self.add_to_cart_button.click()

    def click_view_cart_button(self):
        self.view_cart_button.first.click()

    def verify_product_page_visible(self):
        return self.page.title() == "Automation Exercise"
    
    # New method to verify 'Write Your Review' is visible
    def verify_write_your_review_visible(self):
        expect(self.review_section_title).to_be_visible()

    # New method to enter review details
    def enter_review_details(self, name: str, email: str, review: str):
        self.review_name_input.fill(name)
        self.review_email_input.fill(email)
        self.review_textarea.fill(review)

    # New method to click 'Submit' button
    def click_submit_review_button(self):
        self.submit_review_button.click()

    # New method to verify success message after review submission
    def verify_review_submission_success_message(self, expected_message: str):
        expect(self.success_message).to_have_text(expected_message)