import pytest
import allure
import os
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from utils.random_string_generator import generate_random_string
from pages.products_page import ProductsPage

@pytest.mark.usefixtures("page")
@allure.feature("Products")
@allure.story("TC21_Add_Review_On_Product_Test")
def test_add_review_on_product(page: Page):
    home_page = HomePage(page)
    product_page = ProductsPage(page)
    product_details_page = ProductDetailsPage(page)

    # Create a directory for the test case screenshots
    test_case_name = "test_add_review_on_product"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots", test_case_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    with allure.step("Step 1-2: Launch browser and navigate to the home page"):
        home_page.goto_home_page()
        home_page.accept_cookies()
        screenshot_path = os.path.join(screenshots_dir, "step_1_2_home_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Home Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 3: Click on 'Products' button"):
        home_page.click_products_button()
        screenshot_path = os.path.join(screenshots_dir, "step_3_products_button_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Products Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Verify user is navigated to ALL PRODUCTS page successfully"):
        product_page.verify_all_products_page()
        screenshot_path = os.path.join(screenshots_dir, "step_4_all_products_page.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="All Products Page Verified", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: Click on 'View Product' button for the first product"):
        product_page.click_first_product_view_button()
        screenshot_path = os.path.join(screenshots_dir, "step_5_view_product_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="View Product Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 6: Verify 'Write Your Review' is visible"):
        product_details_page.verify_write_your_review_visible()
        screenshot_path = os.path.join(screenshots_dir, "step_6_write_review_visible.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Write Your Review Visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 7: Enter name, email, and review"):
        review_name = generate_random_string(8)
        review_email = f"{generate_random_string(8)}@example.com"
        review_text = "This is a great product!"
        product_details_page.enter_review_details(name=review_name, email=review_email, review=review_text)
        screenshot_path = os.path.join(screenshots_dir, "step_7_review_details_entered.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Review Details Entered", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 8: Click 'Submit' button"):
        product_details_page.click_submit_review_button()
        screenshot_path = os.path.join(screenshots_dir, "step_8_submit_review_clicked.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Submit Review Button Clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 9: Verify success message 'Thank you for your review.'"):
        product_details_page.verify_review_submission_success_message('Thank you for your review.')
        screenshot_path = os.path.join(screenshots_dir, "step_9_review_submission_success.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Review Submission Success Message", attachment_type=allure.attachment_type.PNG)
