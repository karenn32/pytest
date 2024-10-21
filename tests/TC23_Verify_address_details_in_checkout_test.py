import pytest
import allure
import os
from playwright.sync_api import Page
from utils.random_string_generator import generate_random_string
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from pages.signup_page import SignupPage

@pytest.mark.usefixtures("page")
@allure.feature("Checkout Address Verification")
@allure.story("TC23_Verify_Address_Details_In_Checkout")
def test_verify_address_details_in_checkout(page: Page):
    home_page = HomePage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    login_page = LoginPage(page)
    product_details_page = ProductDetailsPage(page)
    signup_page = SignupPage(page)

    # Generate random strings for name and email
    random_name = generate_random_string(8)
    random_email = f"{generate_random_string(8)}@example.com"

    # Generate random address details
    address_details = {
        "first_name": generate_random_string(6),
        "last_name": generate_random_string(6),
        "company": generate_random_string(10),
        "address1": f"{generate_random_string(8)} Street",
        "address2": f"Suite {generate_random_string(3, digits_only=True)}",
        "country": "United States",
        "state": generate_random_string(8),
        "city": generate_random_string(8),
        "zipcode": generate_random_string(5, digits_only=True),
        "mobile_number": generate_random_string(10, digits_only=True)
    }

    # Create a directory for the test case screenshots
    test_case_name = "TC23_Verify_Address_Details_In_Checkout"
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
        allure.attach.file(screenshot_path, name="Home Page Verification", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Click 'Signup / Login' button"):
        home_page.click_signup_login()
        screenshot_path = os.path.join(screenshots_dir, "step_4_signup_login.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Signup/Login Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Fill all details in Signup and create account"):
        login_page.enter_signup_name(random_name)
        login_page.enter_signup_email(random_email)
        login_page.click_signup_button()
        signup_page.select_title("Mr")
        signup_page.enter_password("password123")
        signup_page.select_date_of_birth("1", "January", "1990")
        signup_page.enter_address_details(**address_details)
        screenshot_path = os.path.join(screenshots_dir, "step_5_create_account.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Create Account Details", attachment_type=allure.attachment_type.PNG)
        signup_page.click_create_account_button()

    with allure.step("Step 6: Verify 'ACCOUNT CREATED!' and click 'Continue' button"):
        signup_page.verify_account_created_title_text('Account Created!')
        screenshot_path = os.path.join(screenshots_dir, "step_6_account_created.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Account Created", attachment_type=allure.attachment_type.PNG)
        signup_page.click_continue()

    with allure.step("Step 7: Verify 'Logged in as username' at the top"):
        home_page.verify_logged_in_user(random_name)
        screenshot_path = os.path.join(screenshots_dir, "step_7_logged_in_user.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Logged In As User", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Add products to cart"):
        home_page.click_view_product_button()
        product_details_page.set_product_quantity(2)
        product_details_page.click_add_to_cart_button()
        product_details_page.click_view_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_8_products_added.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products Added to Cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Click 'Cart' button"):
        home_page.click_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_9_cart_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 10: Verify that cart page is displayed"):
        cart_page.verify_cart_page_displayed()
        screenshot_path = os.path.join(screenshots_dir, "step_10_cart_page_displayed.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Page Displayed", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 11: Click 'Proceed To Checkout'"):
        cart_page.click_proceed_to_checkout()
        screenshot_path = os.path.join(screenshots_dir, "step_11_proceed_to_checkout.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Proceed To Checkout Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 12-13: Verify Address Details and Review Your Order"):
        checkout_page.verify_address_details()
        checkout_page.verify_review_order()
        screenshot_path = os.path.join(screenshots_dir, "step_12_13_verify_address_review.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Address and Order Review", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 14: Click 'Delete Account' button"):
        home_page.click_delete_account()
        screenshot_path = os.path.join(screenshots_dir, "step_14_delete_account.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Delete Account Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 15: Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
        signup_page.verify_account_deleted_title_text("Account Deleted!")
        screenshot_path = os.path.join(screenshots_dir, "step_15_account_deleted.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Account Deleted", attachment_type=allure.attachment_type.PNG)
        signup_page.click_continue()
