import pytest
import allure
import os
from playwright.sync_api import Page
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("page")
@allure.feature("Products")
@allure.story("TC8_Verify_all_products_test")
def test_verify_all_products_and_product_detail_page(page: Page):
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    product_details_page = ProductDetailsPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "TC8_Verify_all_products_test"
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

    with allure.step("Step 6: Verify the products list is visible"):
        products_page.verify_products_list_is_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_6_products_list_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products List Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Click on 'View Product' of the first product"):
        products_page.click_first_product_view_button()
        screenshot_path = os.path.join(screenshots_dir, "step_7_view_first_product.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="View First Product Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8-9: Verify that user is landed to product detail page and the details are visible"):
        product_details_page.verify_product_details(
            name="Blue Top",
            category="Women > Tops",
            price="Rs. 500",
            availability="In Stock",
            condition="New",
            brand="Polo"
        )
        screenshot_path = os.path.join(screenshots_dir, "step_8_9_product_details_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Product Details Visible", attachment_type=allure.attachment_type.PNG)
