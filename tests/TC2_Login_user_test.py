import pytest
import allure
import os
from utils.api_utils import create_user_via_api
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.home_page import HomePage
from utils.random_string_generator import generate_random_string

@pytest.mark.usefixtures("page")
@allure.feature("User Registration and Login")
@allure.story("TC2_Login_user_test")
def test_register_user(page: Page):
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    home_page = HomePage(page)

    # Create a directory for the test case screenshots
    test_case_name = "TC2_Login_user_test"
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
        allure.attach.file(screenshot_path, name="Login Heading Verified", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Enter correct email address and password"):
        login_page.enter_login_email(random_email)
        login_page.enter_login_password(random_password)
        screenshot_path = os.path.join(screenshots_dir, "step_6_enter_credentials.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Credentials Entered", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Click 'Login' button"):
        login_page.click_login_button()
        screenshot_path = os.path.join(screenshots_dir, "step_7_click_login.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Login Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Verify that 'Logged in as username' is visible"):
        home_page.verify_logged_in_user(random_name)
        screenshot_path = os.path.join(screenshots_dir, "step_8_logged_in_user.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Logged In As User", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Click 'Delete Account' button"):
        home_page.click_delete_account()
        screenshot_path = os.path.join(screenshots_dir, "step_9_delete_account.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Delete Account Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 10: Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button"):
        signup_page.verify_account_deleted_title_text("Account Deleted!")
        signup_page.click_continue()
        screenshot_path = os.path.join(screenshots_dir, "step_10_account_deleted.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Account Deleted", attachment_type=allure.attachment_type.PNG)
