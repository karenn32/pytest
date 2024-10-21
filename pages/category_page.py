from playwright.sync_api import Page, expect

class CategoryPage:
    def __init__(self, page: Page):
        self.page = page
        # Locator for the category page title
        self.category_page_title = page.locator('.features_items h2.title')

    # Method to click on a sub-category under the selected category
    def click_sub_category(self, sub_category_name: str):
        sub_category_locator = self.page.locator(f'a', has_text=sub_category_name)
        sub_category_locator.click()

    # Method to verify the category page title
    def verify_category_page_title(self, expected_title: str):
        expect(self.category_page_title).to_have_text(expected_title)
