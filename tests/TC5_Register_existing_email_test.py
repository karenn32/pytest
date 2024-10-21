import pytest
import allure
import os
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("page")
@allure.feature("User Registration and Login")
@allure.story("TC5_Register_existing_email_test")
def test_register_existing_email(page: Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    # Create a directory for the test case screenshots
    test_case_name = "TC5_Register_existing_email_test"
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

    with allure.step("Step 6-7: Enter existing email and name, then click 'Signup' button"):
        login_page.enter_signup_email('brgdpfv@gmail.com')
        login_page.enter_signup_name('brgdpfv')
        login_page.click_signup_button()
        screenshot_path = os.path.join(screenshots_dir, "step_6_7_existing_user.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Existing User Signup Attempt", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify error message 'Email Address already exist!' is displayed"):
        login_page.verify_signup_error_message('Email Address already exist!')
        screenshot_path = os.path.join(screenshots_dir, "step_8_error_message.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Error Message Displayed", attachment_type=allure.attachment_type.PNG)
