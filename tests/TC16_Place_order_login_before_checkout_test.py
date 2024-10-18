import pytest
import allure
import os
from playwright.sync_api import Page
from utils.api_utils import create_user_via_api
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
@allure.story("TC16_Place_Order_Login_Before_Checkout")
def test_place_order_login_before_checkout(page: Page):
    home_page = HomePage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    login_page = LoginPage(page)
    payment_page = PaymentPage(page)
    product_details_page = ProductDetailsPage(page)
    signup_page = SignupPage(page)
    payment_done_page = PaymentDonePage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_place_order_login_before_checkout"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    # Create new user
    random_email = f"{generate_random_string(8)}@example.com"
    random_name = generate_random_string(8)
    random_password = generate_random_string(8)

    with allure.step("Create user via API"):
        create_user_via_api(name=random_name, email=random_email, password=random_password)
        allure.attach(f"Name: {random_name}\nEmail: {random_email}\nPassword: {random_password}", 
                      name="User Data", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Step 1-2: Navigate to main page"):
        home_page.goto_home_page()
        home_page.accept_cookies()
        screenshot_path = os.path.join(screenshots_dir, "step_1_2_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 3: Verify that home page is visible"):
        home_page.verify_home_page_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_3_home_page_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Click 'Signup / Login' button"):
        home_page.click_signup_login()
        screenshot_path = os.path.join(screenshots_dir, "step_4_signup_login_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Signup/Login Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Fill email, password and click 'Login' button"):
        login_page.enter_login_email(random_email)
        login_page.enter_login_password(random_password)
        login_page.click_login_button()
        screenshot_path = os.path.join(screenshots_dir, "step_5_login_attempt.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Login Attempt", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Verify 'Logged in as username' at the top"):
        home_page.verify_logged_in_user(random_name)
        screenshot_path = os.path.join(screenshots_dir, "step_6_logged_in_user.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Logged In As User", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Add products to cart"):
        home_page.click_view_product_button()
        product_details_page.set_product_quantity(2)
        product_details_page.click_add_to_cart_button()
        product_details_page.click_view_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_7_products_added_to_cart.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products Added to Cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Click 'Cart' button"):
        home_page.click_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_8_cart_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Verify that cart page is displayed"):
        cart_page.verify_cart_page_displayed()
        screenshot_path = os.path.join(screenshots_dir, "step_9_cart_page_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Page Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 10: Click 'Proceed To Checkout'"):
        cart_page.click_proceed_to_checkout()
        screenshot_path = os.path.join(screenshots_dir, "step_10_proceed_to_checkout.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Proceed To Checkout Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 11: Verify Address Details and Review Your Order"):
        checkout_page.verify_address_details()
        checkout_page.verify_review_order()
        screenshot_path = os.path.join(screenshots_dir, "step_11_address_details_verified.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Address Details Verified", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 12: Enter description in comment text area and click 'Place Order'"):
        checkout_page.add_order_comment("Please deliver between 9 AM - 12 PM.")
        checkout_page.click_place_order_button()
        screenshot_path = os.path.join(screenshots_dir, "step_12_order_placed.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Order Placed", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 13: Fill in payment details and click Confirm"):
        payment_page.enter_payment_details(
            random_name,
            generate_random_string(16, digits_only=True),
            generate_random_string(3, digits_only=True),
            "12",
            "2025"
        )
        payment_page.click_pay_and_confirm_order()
        screenshot_path = os.path.join(screenshots_dir, "step_13_payment_confirmed.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Payment Confirmed", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 14: Verify success message 'Your order has been placed successfully!'"):
        payment_done_page.verify_order_confirmation_message()
        screenshot_path = os.path.join(screenshots_dir, "step_14_order_successful.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Order Successful", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 15: Click 'Delete Account' button"):
        home_page.click_delete_account()
        screenshot_path = os.path.join(screenshots_dir, "step_15_delete_account.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Delete Account Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 16: Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button"):
        signup_page.verify_account_deleted_title_text("Account Deleted!")
        signup_page.click_continue()
        screenshot_path = os.path.join(screenshots_dir, "step_16_account_deleted.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Account Deleted", attachment_type=allure.attachment_type.PNG)
