import pytest
import allure
import os
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("page")
@allure.feature("Subscription")
@allure.story("TC11_Verify_subscription_cartpage_test")
def test_verify_subscription_in_cart_page(page: Page):
    home_page = HomePage(page)
    cart_page = CartPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "TC11_Verify_subscription_cartpage_test"
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

    with allure.step("Step 4: Click 'Cart' button"):
        home_page.click_cart_button()
        screenshot_path = os.path.join(screenshots_dir, "step_4_cart_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Cart Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Verify text 'SUBSCRIPTION' is visible"):
        cart_page.verify_subscription_text_is_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_6_subscription_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Subscription Text Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Enter email address in input and click arrow button"):
        cart_page.subscribe_with_email("test@example.com")
        screenshot_path = os.path.join(screenshots_dir, "step_7_email_submitted.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Email Submitted", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Verify success message 'You have been successfully subscribed!' is visible"):
        cart_page.verify_subscription_success_message("You have been successfully subscribed!")
        screenshot_path = os.path.join(screenshots_dir, "step_8_success_message.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Success Message Visible", attachment_type=allure.attachment_type.PNG)
