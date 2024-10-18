from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.subscription_text = self.page.locator("text=SUBSCRIPTION")
        self.email_input = self.page.locator("#susbscribe_email")
        self.subscribe_button = self.page.locator("#subscribe")
        self.success_message = self.page.locator("#success-subscribe .alert-success")
        self.cart_items_table = page.locator('#cart_info_table')  # Table containing cart items
        self.cart_items = page.locator('#cart_info_table tbody tr')  # Rows for each product in the cart
        self.product_names = self.cart_items.locator('.cart_description h4 a')  # Product names
        self.product_prices = self.cart_items.locator('.cart_price p')  # Product prices
        self.product_quantities = self.cart_items.locator('.cart_quantity button')  # Product quantities
        self.product_totals = self.cart_items.locator('.cart_total .cart_total_price')  # Total price per product
        self.cart_product_quantity = page.locator('tr#product-1 .cart_quantity button')
        self.proceed_to_checkout_button = page.locator('a.btn.btn-default.check_out')
        self.cart_page_heading = page.locator('.breadcrumb', has_text="Shopping Cart")
        self.remove_product_button = page.locator('.cart_quantity_delete')


    def verify_cart_page_displayed(self):
        expect(self.cart_page_heading).to_be_visible()

    def click_proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()

    def verify_subscription_text_is_visible(self):
        assert self.subscription_text.is_visible()

    def subscribe_with_email(self, email: str):
        self.email_input.fill(email)
        self.subscribe_button.click()

    def verify_subscription_success_message(self, message: str):
        assert self.success_message.inner_text() == message

    # Method to count the number of items in the cart
    def count_cart_items(self):
        return self.cart_items.count()

    # Method to verify product names in the cart
    def verify_product_names(self, expected_names: list):
        product_names = self.product_names.all_text_contents()
        assert product_names == expected_names, f"Expected product names {expected_names}, but got {product_names}"

    # Method to verify product prices in the cart
    def verify_product_prices(self, expected_prices: list):
        product_prices = self.product_prices.all_text_contents()
        assert product_prices == expected_prices, f"Expected prices {expected_prices}, but got {product_prices}"

    # Method to verify product quantities in the cart
    def verify_product_quantities(self, expected_quantities: list):
        product_quantities = self.product_quantities.all_text_contents()
        assert product_quantities == expected_quantities, f"Expected quantities {expected_quantities}, but got {product_quantities}"

    # Method to verify total prices for each product
    def verify_product_totals(self, expected_totals: list):
        product_totals = self.product_totals.all_text_contents()
        assert product_totals == expected_totals, f"Expected totals {expected_totals}, but got {product_totals}"

    # Method to verify the product quantity in the cart
    def verify_product_quantity_in_cart(self, expected_quantity: int):
        actual_quantity = int(self.cart_product_quantity.text_content().strip())
        assert actual_quantity == expected_quantity, f"Expected quantity '{expected_quantity}' but got '{actual_quantity}'"

     # Method to click the 'X' button to remove a product from the cart
    def click_remove_product_button(self):
        self.remove_product_button.click()

    # Method to verify that the product is removed from the cart
    def verify_product_removed_from_cart(self):
        expect(self.product_names).not_to_be_visible()