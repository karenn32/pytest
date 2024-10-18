import pytest
import allure
import os
from playwright.sync_api import Page
from utils.api_utils import create_user_via_api
from utils.random_string_generator import generate_random_string
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("page")
@allure.feature("Products")
@allure.story("TC20_Search_Products_And_Verify_Cart_After_Login")
def test_search_products_and_verify_cart_after_login(page: Page):
    home_page = HomePage(page)
    product_page = ProductsPage(page)
    cart_page = CartPage(page)
    login_page = LoginPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_search_products_and_verify_cart_after_login"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    # Create new user
    random_email = f"{generate_random_string(8)}@example.com"
    random_name = generate_random_string(8)
    random_password = generate_random_string(8)
    
    with allure.step("Create new user via API"):
        create_user_via_api(name=random_name, email=random_email, password=random_password)
        allure.attach(f"User Info: Name: {random_name}, Email: {random_email}, Password: {random_password}",
                      name="User Data", attachment_type=allure.attachment_type.TEXT)

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

    with allure.step("Step 4: Verify that user is navigated to ALL PRODUCTS page successfully"):
        product_page.verify_all_products_page()
        screenshot_path = os.path.join(screenshots_dir, "step_4_all_products_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="All Products Page Verified", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Enter product name in search input and click search button"):
        product_page.search_product("t-shirt")
        screenshot_path = os.path.join(screenshots_dir, "step_5_product_searched.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Product Searched", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Verify 'SEARCHED PRODUCTS' is visible"):
        product_page.verify_searched_products_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_6_searched_products_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Searched Products Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Verify all the products related to search are visible"):
        product_page.verify_search_results_contain("t-shirt")
        screenshot_path = os.path.join(screenshots_dir, "step_7_products_related_to_search.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products Related to Search Verified", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Add those products to cart and click continue shopping after each"):
        product_page.add_product_to_cart('all')
        screenshot_path = os.path.join(screenshots_dir, "step_8_products_added_to_cart.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products Added to Cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Click 'Cart' button and verify that products are visible in cart"):
        home_page.click_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_9_cart_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Button Clicked", attachment_type=allure.attachment_type.PNG)
        cart_page.verify_product_names(["Pure Cotton V-Neck T-Shirt", "Green Side Placket Detail T-Shirt", "Premium Polo T-Shirts"])

    with allure.step("Step 10: Click 'Signup / Login' button and submit login details"):
        home_page.click_signup_login()
        login_page.enter_login_email(random_email)
        login_page.enter_login_password(random_password)
        login_page.click_login_button()
        screenshot_path = os.path.join(screenshots_dir, "step_10_login_attempt.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Login Attempt", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 11: Again, go to Cart page"):
        home_page.click_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_11_cart_accessed_after_login.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Accessed After Login", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 12: Verify that those products are visible in cart after login as well"):
        cart_page.verify_product_names(["Pure Cotton V-Neck T-Shirt", "Green Side Placket Detail T-Shirt", "Premium Polo T-Shirts"])
        screenshot_path = os.path.join(screenshots_dir, "step_12_cart_products_verified.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Products Verified After Login", attachment_type=allure.attachment_type.PNG)
