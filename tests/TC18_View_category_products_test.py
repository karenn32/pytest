import pytest
import allure
import os
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.category_page import CategoryPage

@pytest.mark.usefixtures("page")
@allure.feature("Category Management")
@allure.story("TC18_View_Category_Products_Test")
def test_view_category_products(page: Page):
    home_page = HomePage(page)
    category_page = CategoryPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_view_category_products"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    with allure.step("Step 1-2: Launch browser and navigate to the home page"):
        home_page.goto_home_page()
        home_page.accept_cookies()
        screenshot_path = os.path.join(screenshots_dir, "step_1_2_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 3: Verify that categories are visible on left side bar"):
        home_page.verify_categories_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_3_categories_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Categories Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Click on 'Women' category"):
        home_page.click_category_women()
        screenshot_path = os.path.join(screenshots_dir, "step_4_women_category_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Women Category Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Click on 'Dress' sub-category under 'Women' category"):
        home_page.click_sub_category('Dress')
        screenshot_path = os.path.join(screenshots_dir, "step_5_dress_sub_category_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Dress Sub-category Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'"):
        category_page.verify_category_page_title('Women - Dress Products ')
        screenshot_path = os.path.join(screenshots_dir, "step_6_category_page_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Category Page Title Verified", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Click on 'Men' category"):
        home_page.click_category_men()
        screenshot_path = os.path.join(screenshots_dir, "step_7_men_category_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Men Category Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Click on 'Tshirts' sub-category under 'Men' category"):
        category_page.click_sub_category('Tshirts')
        screenshot_path = os.path.join(screenshots_dir, "step_8_tshirts_sub_category_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Tshirts Sub-category Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Verify that user is navigated to 'Men - Tshirts Products' category page"):
        category_page.verify_category_page_title('Men - Tshirts Products')
        screenshot_path = os.path.join(screenshots_dir, "step_9_category_page_verified.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Men Tshirts Category Page Verified", attachment_type=allure.attachment_type.PNG)
