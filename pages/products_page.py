from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.products_button = page.locator('a[href="/products"]')
        self.all_products_heading = page.locator('h2.title.text-center', has_text="All Products")
        self.product_list = page.locator('.features_items')
        self.first_product_view_button = page.locator('.features_items .product-image-wrapper .choose a', has_text="View Product")
        self.search_input = page.locator('#search_product')
        self.search_button = page.locator('#submit_search')
        self.searched_products_heading = page.locator('h2.title.text-center', has_text="Searched Products")
        self.searched_product_list = page.locator('.features_items .product-image-wrapper')
        self.searched_product_names = page.locator('.features_items .product-image-wrapper .productinfo p')
        self.continue_shopping_button = page.locator('button.btn.btn-success')
        self.view_cart_button = page.locator('a:has-text("View Cart")')
        self.brands_section = page.locator('.left-sidebar h2', has_text="Brands")
        self.searched_products_heading = page.locator('h2.title', has_text="Searched Products")
        self.product_items = page.locator('.productinfo')
        self.add_to_cart_buttons = page.locator('.btn.btn-default.add-to-cart')

    
    # Method to navigate to the Products page
    def goto(self):
        self.page.goto('http://automationexercise.com/products')

    # Method to click on the 'Products' button from the home page
    def click_products_button(self):
        self.products_button.click()

    # Method to verify that the "All Products" page is visible
    def verify_all_products_page(self):
        expect(self.all_products_heading).to_be_visible()

    # Method to verify the product list is visible
    def verify_products_list_is_visible(self):
        expect(self.product_list).to_be_visible()

    # Method to click on 'View Product' for the first product
    def click_first_product_view_button(self):
        self.first_product_view_button.first.click()

    # Method to search for a product
    def search_product(self, product_name: str):
        self.search_input.fill(product_name)
        self.search_button.click()

    # Method to verify that 'Searched Products' is visible
    def verify_searched_products_heading(self):
        expect(self.searched_products_heading).to_be_visible()

    # Method to verify that the searched products list is visible
    def verify_searched_products_list_is_visible(self):
        expect(self.searched_product_list).to_be_visible()

    # Method to verify that all searched products are related to the search term
    def verify_searched_products_related_to(self, search_term: str):
        product_names = self.searched_product_names.all_text_contents()
        for name in product_names:
            assert search_term.lower() in name.lower(), f"Product '{name}' does not match the search term '{search_term}'"
    
    def click_continue_shopping(self):
        self.continue_shopping_button.click()

    def click_view_cart(self):
        self.view_cart_button.click()

    # Method to verify that brands are visible on the left sidebar
    def verify_brands_visible(self):
        expect(self.brands_section).to_be_visible()

    # Method to click on a specific brand by name
    def click_brand(self, brand_name: str):
        brand_locator = self.page.locator(f'a', has_text=brand_name)
        brand_locator.click()

    # Method to verify that 'SEARCHED PRODUCTS' heading is visible
    def verify_searched_products_visible(self):
        expect(self.searched_products_heading).to_be_visible()

    # Method to verify that all search results contain a specific term
    def verify_search_results_contain(self, search_term: str):
        for product_item in self.product_items.all_text_contents():
            assert search_term.lower() in product_item.lower(), f"Product '{product_item}' does not contain '{search_term}'"

    # Method to add products to cart
    def add_product_to_cart(self, product_number):
        if product_number == "all":
            # If 'all' is passed, click on all "Add to Cart" buttons
            add_to_cart_buttons = self.page.locator('.productinfo a.add-to-cart')
            product_count = add_to_cart_buttons.count()
        
            for index in range(product_count):
                button = add_to_cart_buttons.nth(index)
                button.click()
                 # Wait for the modal to be visible before clicking continue shopping
                self.page.locator('.close-modal').wait_for(state='visible')
                self.page.locator('.close-modal').click()  # Click continue shopping
        else:
            # If a specific product number is provided, add that product to the cart
            add_to_cart_button = self.page.locator(f'.productinfo a[data-product-id="{product_number}"]')
            add_to_cart_button.click()