from playwright.sync_api import Page, expect

class BrandPage:
    def __init__(self, page: Page):
        self.page = page
        # Locator for the brand page title
        self.brand_page_title = page.locator('.features_items h2.title')

    # Method to verify the brand page title
    def verify_brand_page_title(self, expected_title: str):
        expect(self.brand_page_title).to_have_text(expected_title)
