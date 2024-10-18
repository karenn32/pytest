import pytest
import allure
import os
from playwright.sync_api import Page
from utils.random_string_generator import generate_random_string
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from pages.product_details_page import ProductDetailsPage
from pages.signup_page import SignupPage
from pages.payment_done_page import PaymentDonePage

@pytest.mark.usefixtures("page")
@allure.feature("Order Placement")
@allure.story("TC15_Place_Order_Register_Before_Checkout")
def test_place_order_register_before_checkout(page: Page):
    home_page = HomePage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    login_page = LoginPage(page)
    payment_page = PaymentPage(page)
    product_details_page = ProductDetailsPage(page)
    signup_page = SignupPage(page)
    payment_done_page = PaymentDonePage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_place_order_register_before_checkout"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    # Generate random strings for name and email
    random_name = generate_random_string(8)
    random_email = f"{generate_random_string(8)}@example.com"

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

    with allure.step("Step 4: Click 'Signup / Login' button"):
        home_page.click_signup_login()
        screenshot_path = os.path.join(screenshots_dir, "step_4_signup_login_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Signup/Login Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Fill all details in Signup and create account"):
        login_page.enter_signup_name(random_name)
        login_page.enter_signup_email(random_email)
        login_page.click_signup_button()
        signup_page.select_title("Mr")
        signup_page.enter_password("password123")
        signup_page.select_date_of_birth("1", "January", "1990")
        signup_page.enter_address_details(
            first_name="Test",
            last_name="User",
            company="Test Company",
            address1="123 Test Street",
            address2="Suite 456",
            country="United States",
            state="California",
            city="Los Angeles",
            zipcode="90001",
            mobile_number="1234567890"
        )
        signup_page.click_create_account_button()
        screenshot_path = os.path.join(screenshots_dir, "step_5_signup_details_filled.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Signup Details Filled", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Verify 'ACCOUNT CREATED!' and click 'Continue' button"):
        signup_page.verify_account_created_title_text('Account Created!')
        signup_page.click_continue()
        screenshot_path = os.path.join(screenshots_dir, "step_6_account_created.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Account Created", attachment_type=allure.attachment_type.PNG)

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
        screenshot_path = os.path.join(screenshots_dir, "step_8_products_added_to_cart.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products Added to Cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Click 'Cart' button"):
        home_page.click_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_9_cart_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 10: Verify that cart page is displayed"):
        cart_page.verify_cart_page_displayed()
        screenshot_path = os.path.join(screenshots_dir, "step_10_cart_page_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Page Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 11: Click 'Proceed To Checkout'"):
        cart_page.click_proceed_to_checkout()
        screenshot_path = os.path.join(screenshots_dir, "step_11_proceed_to_checkout.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Proceed To Checkout Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 12: Verify Address Details and Review Your Order"):
        checkout_page.verify_address_details()
        checkout_page.verify_review_order()
        screenshot_path = os.path.join(screenshots_dir, "step_12_address_details_verified.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Address Details Verified", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 13: Enter description in comment text area and click 'Place Order'"):
        checkout_page.add_order_comment(generate_random_string(20))
        checkout_page.click_place_order_button()
        screenshot_path = os.path.join(screenshots_dir, "step_13_order_placed.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Order Placed", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 14: Fill in payment details and click Confirm"):
        payment_page.enter_payment_details(
            random_name,
            generate_random_string(16, digits_only=True),
            generate_random_string(3, digits_only=True),
            "12",
            "2025"
        )
        payment_page.click_pay_and_confirm_order()
        screenshot_path = os.path.join(screenshots_dir, "step_14_payment_confirmed.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Payment Confirmed", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 15: Verify success message 'Your order has been placed successfully!'"):
        payment_done_page.verify_order_confirmation_message()
        screenshot_path = os.path.join(screenshots_dir, "step_15_order_successful.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Order Successful", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 16: Click 'Delete Account' button"):
        home_page.click_delete_account()
        screenshot_path = os.path.join(screenshots_dir, "step_16_delete_account.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Delete Account Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 17: Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button"):
        signup_page.verify_account_deleted_title_text("Account Deleted!")
        signup_page.click_continue()
        screenshot_path = os.path.join(screenshots_dir, "step_17_account_deleted.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Account Deleted", attachment_type=allure.attachment_type.PNG)
