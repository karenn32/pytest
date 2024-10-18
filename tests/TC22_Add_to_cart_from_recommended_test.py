import pytest
import allure
import os
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.products_page import ProductsPage

@pytest.mark.usefixtures("page")
@allure.feature("Cart Management")
@allure.story("TC22_Add_Recommended_Product_To_Cart_Test")
def test_add_recommended_product_to_cart(page: Page):
    home_page = HomePage(page)
    cart_page = CartPage(page)
    products_page = ProductsPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_add_recommended_product_to_cart"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    with allure.step("Step 1-2: Launch browser and navigate to the home page"):
        home_page.goto_home_page()
        home_page.accept_cookies()
        screenshot_path = os.path.join(screenshots_dir, "step_1_2_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Verify 'RECOMMENDED ITEMS' are visible"):
        home_page.verify_recommended_items_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_4_recommended_items_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Recommended Items Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Click on 'Add To Cart' on a recommended product"):
        home_page.click_add_to_cart_on_recommended_product()
        screenshot_path = os.path.join(screenshots_dir, "step_5_add_to_cart_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Add To Cart Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Click on 'View Cart' button"):
        home_page.click_view_cart()
        screenshot_path = os.path.join(screenshots_dir, "step_6_view_cart_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="View Cart Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Verify that the product is displayed in the cart page"):
        cart_page.verify_product_names(['Blue Top'])
        screenshot_path = os.path.join(screenshots_dir, "step_7_product_in_cart.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Product In Cart Verified", attachment_type=allure.attachment_type.PNG)
