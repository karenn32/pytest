import pytest
import allure
import os
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("page")
@allure.feature("Cart Management")
@allure.story("TC13_Verify_product_quantity_in_cart_test")
def test_verify_product_quantity_in_cart(page: Page):
    home_page = HomePage(page)
    product_details_page = ProductDetailsPage(page)
    cart_page = CartPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_verify_product_quantity_in_cart"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    with allure.step("Step 1-2: Launch browser and navigate to the home page"):
        home_page.goto_home_page()
        home_page.accept_cookies()
        screenshot_path = os.path.join(screenshots_dir, "step_1_2_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Click 'View Product' for any product on the home page"):
        home_page.click_view_product_button()
        screenshot_path = os.path.join(screenshots_dir, "step_4_view_product_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="View Product Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Verify product detail is opened"):
        product_details_page.verify_product_page_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_5_product_detail_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Product Detail Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Increase quantity to 4"):
        product_details_page.set_product_quantity(4)
        screenshot_path = os.path.join(screenshots_dir, "step_6_quantity_increased.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Quantity Increased", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Click 'Add to cart' button"):
        product_details_page.click_add_to_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_7_added_to_cart.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Added to Cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Click 'View Cart' button"):
        product_details_page.click_view_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_8_view_cart_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="View Cart Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Verify that product is displayed in cart page with exact quantity"):
        cart_page.verify_product_quantity_in_cart(4)
        screenshot_path = os.path.join(screenshots_dir, "step_9_cart_quantity_verified.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Quantity Verified", attachment_type=allure.attachment_type.PNG)
