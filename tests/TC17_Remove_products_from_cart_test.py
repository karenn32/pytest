import pytest
import allure
import os
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage

@pytest.mark.usefixtures("page")
@allure.feature("Cart Management")
@allure.story("TC17_Remove_Products_From_Cart_Test")
def test_remove_products_from_cart(page: Page):
    home_page = HomePage(page)
    cart_page = CartPage(page)
    product_details_page = ProductDetailsPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "TC17_Remove_Products_From_Cart_Test"
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

    with allure.step("Step 4: Add products to cart"):
        home_page.click_view_product_button()
        product_details_page.set_product_quantity(2)
        product_details_page.click_add_to_cart_button()
        product_details_page.click_view_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_4_product_added_to_cart.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Product Added to Cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Click 'Cart' button"):
        home_page.click_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_5_cart_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Verify that cart page is displayed"):
        cart_page.verify_cart_page_displayed()
        screenshot_path = os.path.join(screenshots_dir, "step_6_cart_page_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Page Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Click 'X' button corresponding to the product"):
        cart_page.click_remove_product_button()
        screenshot_path = os.path.join(screenshots_dir, "step_7_product_removed.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Product Removed", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Verify that product is removed from the cart"):
        cart_page.verify_product_removed_from_cart()
        screenshot_path = os.path.join(screenshots_dir, "step_8_verification_product_removed.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Product Removal Verified", attachment_type=allure.attachment_type.PNG)
