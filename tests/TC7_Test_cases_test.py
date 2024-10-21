import pytest
import allure
import os
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

@pytest.mark.usefixtures("page")
@allure.feature("Navigation")
@allure.story("TC7_Test_cases_test")
def test_verify_test_cases_page(page: Page):
    home_page = HomePage(page)

    # Create a directory for the test case screenshots
    test_case_name = "TC7_Test_cases_test"
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

    with allure.step("Step 4: Click on the 'Test Cases' button"):
        home_page.click_test_cases()
        screenshot_path = os.path.join(screenshots_dir, "step_4_test_cases_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Test Cases Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Verify user is navigated to the test cases page successfully"):
        expect(page).to_have_url('https://automationexercise.com/test_cases')
        screenshot_path = os.path.join(screenshots_dir, "step_5_test_cases_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Test Cases Page Verified", attachment_type=allure.attachment_type.PNG)
