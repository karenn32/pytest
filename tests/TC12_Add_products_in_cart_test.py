import pytest
import allure
import os
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

@pytest.mark.usefixtures("page")
@allure.feature("Cart Management")
@allure.story("TC12_Add_products_in_cart_test")
def test_add_products_to_cart(page):
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_add_products_to_cart"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    with allure.step("Step 1-2: Launch browser and navigate to URL"):
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

    with allure.step("Step 4: Click 'Products' button"):
        home_page.click_products_button()
        screenshot_path = os.path.join(screenshots_dir, "step_4_products_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Hover over the first product and click 'Add to cart'"):
        products_page.add_product_to_cart(1)
        screenshot_path = os.path.join(screenshots_dir, "step_5_first_product_added.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="First Product Added to Cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Click 'Continue Shopping' button"):
        products_page.click_continue_shopping()
        screenshot_path = os.path.join(screenshots_dir, "step_6_continue_shopping_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Continue Shopping Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Hover over the second product and click 'Add to cart'"):
        products_page.add_product_to_cart(2)
        screenshot_path = os.path.join(screenshots_dir, "step_7_second_product_added.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Second Product Added to Cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Click 'View Cart' button"):
        products_page.click_view_cart()
        screenshot_path = os.path.join(screenshots_dir, "step_8_view_cart_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="View Cart Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Verify both products are added to Cart"):
        assert cart_page.count_cart_items() == 2  # Verify that two products are in the cart
        screenshot_path = os.path.join(screenshots_dir, "step_9_cart_items_counted.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Items Counted", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 10: Verify their prices, quantity, and total price"):
        expected_prices = ["Rs. 500", "Rs. 400"] 
        expected_quantities = ["1", "1"] 
        expected_totals = ["Rs. 500", "Rs. 400"] 
        
        cart_page.verify_product_prices(expected_prices)
        cart_page.verify_product_quantities(expected_quantities)
        cart_page.verify_product_totals(expected_totals)
        screenshot_path = os.path.join(screenshots_dir, "step_10_product_details_verified.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Product Details Verified", attachment_type=allure.attachment_type.PNG)
