from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.login_email = page.locator('[data-qa="login-email"]')
        self.login_password = page.locator('[data-qa="login-password"]')
        self.login_button = page.locator('[data-qa="login-button"]')
        self.signup_button = page.locator('[data-qa="signup-button"]')
        self.signup_name = page.locator('[data-qa="signup-name"]')
        self.signup_email = page.locator('[data-qa="signup-email"]')
        self.signup_form_heading = page.locator('.signup-form h2')
        self.login_form_heading = page.locator('.login-form h2')
        self.login_error_message = page.locator('.login-form p[style="color: red;"]')
        self.signup_error_message = page.locator('.signup-form p[style="color: red;"]')
        self.continue_button = page.locator('[data-qa=continue-button]')
        self.account_deleted_title = page.locator('[data-qa="account-deleted"] b')

    # Methods
    def enter_login_email(self, email: str):
        self.login_email.fill(email)

    def goto(self):
        self.page.goto('https://automationexercise.com/login')

    def enter_login_password(self, password: str):
        self.login_password.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def enter_signup_name(self, name: str):
        self.signup_name.fill(name)

    def enter_signup_email(self, email: str):
        self.signup_email.fill(email)

    def click_signup_button(self):
        self.signup_button.click()

    def verify_signup_form_heading(self, expected_text: str):
        expect(self.signup_form_heading).to_have_text(expected_text)
    
    def verify_login_form_heading(self, expected_text: str):
        expect(self.login_form_heading).to_have_text(expected_text)

    def verify_login_error_message(self, expected_text: str):
        expect(self.login_error_message).to_be_visible()
        expect(self.login_error_message).to_have_text(expected_text)

    def verify_signup_error_message(self, expected_text: str):
        expect(self.signup_error_message).to_be_visible()
        expect(self.signup_error_message).to_have_text(expected_text)

    def verify_account_deleted_title_text(self, expected_text: str):
        expect(self.account_deleted_title).to_have_text(expected_text)

    def click_continue(self):
        self.continue_button.click()