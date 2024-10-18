import pytest
import allure
import os
from playwright.sync_api import Page
from pages.products_page import ProductsPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("page")
@allure.feature("Products Search")
@allure.story("TC9_Search_product_test")
def test_search_product(page: Page):
    products_page = ProductsPage(page)
    home_page = HomePage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_search_product"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    with allure.step("Step 1-2: Launch browser and navigate to the home page"):
        home_page.goto_home_page()
        home_page.accept_cookies()
        screenshot_path = os.path.join(screenshots_dir, "step_1_2_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 3: Verify that home page is visible successfully"):
        home_page.verify_home_page_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_3_home_page_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Click on 'Products' button"):
        products_page.click_products_button()
        screenshot_path = os.path.join(screenshots_dir, "step_4_products_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Verify user is navigated to ALL PRODUCTS page successfully"):
        products_page.verify_all_products_page()
        screenshot_path = os.path.join(screenshots_dir, "step_5_all_products_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="All Products Page Verified", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Enter product name in search input and click search button"):
        products_page.search_product("Blue Top")
        screenshot_path = os.path.join(screenshots_dir, "step_6_product_searched.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Product Searched", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Verify 'SEARCHED PRODUCTS' is visible"):
        products_page.verify_searched_products_heading()
        screenshot_path = os.path.join(screenshots_dir, "step_7_searched_products_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Searched Products Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Verify that all the products related to search are visible"):
        products_page.verify_searched_products_related_to("Blue Top")
        screenshot_path = os.path.join(screenshots_dir, "step_8_products_related_to_search.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products Related to Search Visible", attachment_type=allure.attachment_type.PNG)
