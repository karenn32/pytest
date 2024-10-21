import pytest
import allure
import os
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.home_page import HomePage
from utils.random_string_generator import generate_random_string

@pytest.mark.usefixtures("page")
@allure.feature("User Registration and Login")
@allure.story("TC4_Logout_user_test")
def test_register_user(page: Page):
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    home_page = HomePage(page)

    random_email = f"{generate_random_string(8)}@example.com"
    random_name = generate_random_string(8)

    # Create a directory for the test case screenshots
    test_case_name = "TC4_Logout_user_test"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    with allure.step("Step 1-2: Launch browser and navigate to URL"):
        page.goto('http://automationexercise.com')
        home_page.accept_cookies()
        screenshot_path = os.path.join(screenshots_dir, "step_1_2_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 3: Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")
        screenshot_path = os.path.join(screenshots_dir, "step_3_verify_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page Verification", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Click on 'Signup / Login' button"):
        home_page.click_signup_login()
        screenshot_path = os.path.join(screenshots_dir, "step_4_click_signup_login.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Signup/Login Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Verify 'Login to your account' is visible"):
        login_page.verify_login_form_heading('Login to your account')
        screenshot_path = os.path.join(screenshots_dir, "step_5_verify_login_heading.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Login Form Heading", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6-7: Enter name and email address, then click 'Signup' button"):
        login_page.enter_signup_name(random_name)
        login_page.enter_signup_email(random_email)
        login_page.click_signup_button()
        screenshot_path = os.path.join(screenshots_dir, "step_6_7_signup_attempt.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Signup Attempt", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Verify that 'ENTER ACCOUNT INFORMATION' is visible"):
        signup_page.verify_login_form_heading_text('Enter Account Information')
        screenshot_path = os.path.join(screenshots_dir, "step_8_enter_account_information.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Account Information Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Fill details: Title, Name, Email, Password, Date of birth"):
        signup_page.select_title("Mr")
        signup_page.enter_password("password123")
        signup_page.select_date_of_birth("1", "January", "1990")
        screenshot_path = os.path.join(screenshots_dir, "step_9_fill_details.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Details Filled", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 10-11: Select checkboxes for newsletter and offers"):
        signup_page.check_newsletter()
        signup_page.check_offers()
        screenshot_path = os.path.join(screenshots_dir, "step_10_11_check_newsletter_offers.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Checkboxes Selected", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 12: Fill address details"):
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
        screenshot_path = os.path.join(screenshots_dir, "step_12_fill_address.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Address Details Filled", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 13: Click 'Create Account' button"):
        signup_page.click_create_account_button()
        screenshot_path = os.path.join(screenshots_dir, "step_13_create_account.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Create Account Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 14: Verify that 'ACCOUNT CREATED!' is visible"):
        signup_page.verify_account_created_title_text('Account Created!')
        screenshot_path = os.path.join(screenshots_dir, "step_14_account_created.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Account Created", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 15: Click 'Continue' button"):
        signup_page.click_continue()
        screenshot_path = os.path.join(screenshots_dir, "step_15_continue.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Continue Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 17: Click 'Logout' button"):
        home_page.click_logout()
        expect(page).to_have_url('https://automationexercise.com/login')
        screenshot_path = os.path.join(screenshots_dir, "step_17_logout.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Logout Successful", attachment_type=allure.attachment_type.PNG)
