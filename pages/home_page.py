from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.signup_login_button = self.page.locator('a[href="/login"]')
        self.accept_cookies_button = self.page.locator('button.fc-cta-consent')
        self.logged_in_user = self.page.locator("li:has-text('Logged in as') b")
        self.delete_account = self.page.locator("li:has-text('Delete Account')")
        self.logout = self.page.locator("li:has-text('Logout')")
        self.contact_us = self.page.locator("header li:nth-child(8)")
        self.test_cases = self.page.locator('header li:nth-child(5)')
        self.homepage_logo = page.locator('img[src*="logo.png"]')
        self.homepage_logo = page.locator('img[src*="logo.png"]')
        self.subscription_text = page.locator('h2', has_text="Subscription")
        self.subscription_email_input = page.locator('#susbscribe_email')
        self.subscription_button = page.locator('#subscribe')
        self.subscription_success_message = self.page.locator('#success-subscribe .alert-success')
        self.cart_button = page.locator('header li:nth-child(3)')
        self.products_button = page.locator('a[href="/products"]')
        self.view_product_button = page.locator('.features_items .product-image-wrapper .choose a', has_text="View Product")
        self.categories_section = page.locator('.left-sidebar h2', has_text="Category")
        self.women_category = page.locator('a[data-toggle="collapse"][data-parent="#accordian"][href="#Women"]')
        self.men_category = page.locator('a[data-toggle="collapse"][data-parent="#accordian"][href="#Men"]')
        self.recommended_items_section = page.locator('h2', has_text="Recommended items")
        self.recommended_add_to_cart_button = page.locator('.recommended_items .btn.btn-default.add-to-cart')
        self.view_cart_button = page.locator('a[href="/view_cart"]', has_text="View cart")
        self.subscription_section = page.locator('h2', has_text="Subscription")
        self.scroll_up_button = page.locator('a[id=scrollUp]')
        self.carousel_elements = page.locator('.carousel-inner .item h2', has_text="Full-Fledged practice website for Automation Engineers")


    def goto_home_page(self):
        self.page.goto("http://automationexercise.com")

    def verify_home_page_visible(self):
        return self.page.title() == "Automation Exercise"

    def click_signup_login(self):
        self.signup_login_button.first.click()

    def click_delete_account(self):
        self.delete_account.click()

    def click_logout(self):
        self.logout.click()

    def click_cart_button(self):
        self.cart_button.click()


    def click_test_cases(self):
        self.test_cases.click()
        
    def accept_cookies(self):
        if self.accept_cookies_button.is_visible():
            self.accept_cookies_button.click()

    def verify_logged_in_user(self, expected_text: str):
        expect(self.logged_in_user).to_have_text(expected_text)

    def click_contact_us(self):
        self.contact_us.click()

    def verify_subscription_text_is_visible(self):
        expect(self.subscription_text).to_be_visible()

    def subscribe_with_email(self, email: str):
        self.subscription_email_input.fill(email)
        self.subscription_button.click()

    def verify_subscription_success_message(self, expected_message: str):
        expect(self.subscription_success_message).to_have_text(expected_message)

    def click_products_button(self):
        self.products_button.click()

    def click_view_product_button(self):
        self.view_product_button.first.click()

    # Method to verify that categories are visible on the left sidebar
    def verify_categories_visible(self):
        expect(self.categories_section).to_be_visible()

    # Method to click on 'Women' category
    def click_category_women(self):
        self.women_category.click()

    # Method to click on 'Men' category
    def click_category_men(self):
        self.men_category.click()

    # Method to click on a specific sub-category under the selected category
    def click_sub_category(self, sub_category_name: str):
        sub_category_locator = self.page.locator(f'li a[href="/category_products/1"]', has_text=sub_category_name)
        sub_category_locator.click()

        # Method to verify that 'RECOMMENDED ITEMS' are visible
    def verify_recommended_items_visible(self):
        expect(self.recommended_items_section).to_be_visible()

    # Method to click on 'Add To Cart' on the first recommended product
    def click_add_to_cart_on_recommended_product(self):
        self.recommended_add_to_cart_button.first.click()

    def click_view_cart(self):
        self.view_cart_button.click()

       # Method to scroll down to the bottom of the page
    def scroll_to_bottom(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Method to click the scroll-up arrow button
    def click_scroll_up_button(self):
        self.scroll_up_button.click()

    # Method to verify that any one of the carousel elements is visible on the screen
    def verify_any_carousel_element_visible(self):
        for i in range(self.carousel_elements.count()):
            element = self.carousel_elements.nth(i)
            if element.is_visible() and element.bounding_box() is not None:
                print(f"Carousel element {i+1} is visible on the screen.")
                return True
        raise AssertionError("None of the carousel elements are visible on the screen")
    
        # Method to scroll up to the top of the page
    def scroll_to_top(self):
        self.page.evaluate("window.scrollTo(0, 0)")