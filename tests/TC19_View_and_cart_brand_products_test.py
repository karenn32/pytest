import pytest
import allure
import os
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.brand_page import BrandPage

@pytest.mark.usefixtures("page")
@allure.feature("Products")
@allure.story("TC19_View_And_Cart_Brand_Products_Test")
def test_view_and_cart_brand_products(page: Page):
    home_page = HomePage(page)
    product_page = ProductsPage(page)
    brand_page = BrandPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "TC19_View_And_Cart_Brand_Products_Test"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    with allure.step("Step 1-2: Launch browser and navigate to the home page"):
        home_page.goto_home_page()
        home_page.accept_cookies()
        screenshot_path = os.path.join(screenshots_dir, "step_1_2_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 3: Click on 'Products' button"):
        home_page.click_products_button()
        screenshot_path = os.path.join(screenshots_dir, "step_3_products_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Verify that Brands are visible on the left side bar"):
        product_page.verify_brands_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_4_brands_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Brands Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Click on 'Polo' brand"):
        product_page.click_brand('Polo')
        screenshot_path = os.path.join(screenshots_dir, "step_5_polo_brand_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Polo Brand Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Verify user is navigated to brand page and products are displayed"):
        brand_page.verify_brand_page_title('Brand - Polo Products')
        screenshot_path = os.path.join(screenshots_dir, "step_6_polo_brand_page_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Polo Brand Page Verified", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Click on 'H&M' brand"):
        product_page.click_brand('H&M')
        screenshot_path = os.path.join(screenshots_dir, "step_7_hm_brand_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="H&M Brand Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Verify user is navigated to H&M brand page and products are displayed"):
        brand_page.verify_brand_page_title('Brand - H&M Products')
        screenshot_path = os.path.join(screenshots_dir, "step_8_hm_brand_page_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="H&M Brand Page Verified", attachment_type=allure.attachment_type.PNG)
