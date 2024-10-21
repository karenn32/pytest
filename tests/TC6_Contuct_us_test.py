import pytest
import allure
import os
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.contact_page import ContactUsPage

@pytest.mark.usefixtures("page")
@allure.feature("Contact Us Form")
@allure.story("TC6_Contact_us_test")
def test_contact_us_form(page: Page):
    home_page = HomePage(page)
    contact_page = ContactUsPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "TC6_Contact_us_test"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    with allure.step("Step 1: Launch browser and navigate to home page"):
        home_page.goto_home_page()
        home_page.accept_cookies()
        screenshot_path = os.path.join(screenshots_dir, "step_1_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 2: Verify that home page is visible"):
        expect(page).to_have_title("Automation Exercise")
        screenshot_path = os.path.join(screenshots_dir, "step_2_home_page_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 3: Click on 'Contact Us' button"):
        home_page.click_contact_us()
        screenshot_path = os.path.join(screenshots_dir, "step_3_contact_us_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Contact Us Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Verify 'GET IN TOUCH' is visible"):
        expect(contact_page.contact_form_heading).to_be_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_4_get_in_touch.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="GET IN TOUCH Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Enter name, email, subject, and message"):
        contact_page.fill_contact_form(
            name="Test User",
            email="testuser@example.com",
            subject="Test Subject",
            message="This is a test message."
        )
        screenshot_path = os.path.join(screenshots_dir, "step_5_fill_contact_form.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Contact Form Filled", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Upload file"):
        contact_page.upload_file("files/testfile.txt")
        screenshot_path = os.path.join(screenshots_dir, "step_6_file_uploaded.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="File Uploaded", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Handle alert (click OK button)"):
        page.on("dialog", lambda dialog: dialog.accept())
        screenshot_path = os.path.join(screenshots_dir, "step_7_alert_handled.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Alert Handled", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Click 'Submit' button"):
        contact_page.click_submit_button()
        screenshot_path = os.path.join(screenshots_dir, "step_8_submit_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Submit Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Verify success message is visible"):
        expect(contact_page.success_message).to_be_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_9_success_message.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Success Message Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 10: Click 'Home' button and verify that landed on home page successfully"):
        contact_page.click_home_button()
        expect(page).to_have_url("https://automationexercise.com/")
        expect(page).to_have_title("Automation Exercise")
        screenshot_path = os.path.join(screenshots_dir, "step_10_home_page_verified.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page Verified", attachment_type=allure.attachment_type.PNG)
