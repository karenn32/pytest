import pytest
import allure
import os
from playwright.sync_api import Page
from pages.home_page import HomePage

@pytest.mark.usefixtures("page")
@allure.feature("Subscription")
@allure.story("TC10_Verify_subscription_homepage_test")
def test_verify_subscription_in_home_page(page: Page):
    home_page = HomePage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_verify_subscription_in_home_page"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    with allure.step("Step 1-2: Launch browser and navigate to the home page"):
        home_page.goto_home_page()
        home_page.accept_cookies()
        screenshot_path = os.path.join(screenshots_dir, "step_1_2_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 3: Verify that the home page is visible successfully"):
        home_page.verify_home_page_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_3_home_page_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4-5: Verify text 'SUBSCRIPTION' is visible"):
        home_page.verify_subscription_text_is_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_4_5_subscription_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Subscription Text Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Enter email address in input and click arrow button"):
        home_page.subscribe_with_email("test@example.com")
        screenshot_path = os.path.join(screenshots_dir, "step_6_email_submitted.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Email Submitted", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Verify success message 'You have been successfully subscribed!' is visible"):
        home_page.verify_subscription_success_message("You have been successfully subscribed!")
        screenshot_path = os.path.join(screenshots_dir, "step_7_success_message.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Success Message Visible", attachment_type=allure.attachment_type.PNG)
