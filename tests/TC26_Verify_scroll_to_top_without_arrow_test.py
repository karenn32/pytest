import pytest
import allure
import os
from playwright.sync_api import Page
from pages.home_page import HomePage

@pytest.mark.usefixtures("page")
@allure.feature("Scroll Functionality")
@allure.story("TC16_Verify_Scroll_Up_Without_Arrow_Button")
def test_verify_scroll_up_without_arrow_button(page: Page):
    home_page = HomePage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_verify_scroll_up_without_arrow_button"
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

    with allure.step("Step 4: Scroll down page to bottom"):
        home_page.scroll_to_bottom()
        screenshot_path = os.path.join(screenshots_dir, "step_4_scrolled_down.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Scrolled Down", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Verify 'SUBSCRIPTION' is visible"):
        home_page.verify_subscription_text_is_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_5_subscription_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Subscription Text Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Scroll up page to top without using the arrow button"):
        home_page.scroll_to_top()
        screenshot_path = os.path.join(screenshots_dir, "step_6_scrolled_up.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Scrolled Up Without Arrow", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Verify that page is scrolled up and the target text is visible on screen"):
        home_page.verify_any_carousel_element_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_7_carousel_element_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Carousel Element Visible", attachment_type=allure.attachment_type.PNG)
