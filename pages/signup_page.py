from playwright.sync_api import Page, expect

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.title_mr = page.locator('.radio-inline input[value="Mr"]')
        self.title_mrs = page.locator('.radio-inline input[value="Mrs"]')
        self.password = page.locator('[data-qa="password"]')
        self.days = page.locator('[data-qa="days"]')
        self.months = page.locator('[data-qa="months"]')
        self.years = page.locator('[data-qa="years"]')
        self.newsletter_checkbox = page.locator('#newsletter')
        self.offers_checkbox = page.locator('#optin')
        self.first_name = page.locator('[data-qa="first_name"]')
        self.last_name = page.locator('[data-qa="last_name"]')
        self.company = page.locator('[data-qa="company"]')
        self.address1 = page.locator('[data-qa="address"]')
        self.address2 = page.locator('[data-qa="address2"]')
        self.country = page.locator('[data-qa="country"]')
        self.state = page.locator('[data-qa="state"]')
        self.city = page.locator('[data-qa="city"]')
        self.zipcode = page.locator('[data-qa="zipcode"]')
        self.mobile_number = page.locator('[data-qa="mobile_number"]')
        self.create_account_button = page.locator('[data-qa="create-account"]')
        self.login_form_heading = page.locator('.login-form h2:first-child b')
        self.account_created_title = page.locator('[data-qa="account-created"] b')
        self.continue_button = page.locator('[data-qa=continue-button]')
        self.account_deleted_title = page.locator('[data-qa="account-deleted"] b')

    # Methods
    def select_title(self, title: str):
        if title.lower() == 'mr':
            self.title_mr.click()
        elif title.lower() == 'mrs':
            self.title_mrs.click()

    def enter_password(self, password: str):
        self.password.fill(password)

    def select_date_of_birth(self, day: str, month: str, year: str):
        self.days.select_option(day)
        self.months.select_option(month)
        self.years.select_option(year)

    def check_newsletter(self):
        self.newsletter_checkbox.check()

    def check_offers(self):
        self.offers_checkbox.check()

    def enter_address_details(self, first_name: str, last_name: str, company: str, address1: str, address2: str, country: str, state: str, city: str, zipcode: str, mobile_number: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.company.fill(company)
        self.address1.fill(address1)
        self.address2.fill(address2)
        self.country.select_option(country)
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile_number.fill(mobile_number)

    def click_create_account_button(self):
        self.create_account_button.click()

    def verify_login_form_heading_text(self, expected_text: str):
        expect(self.login_form_heading).to_have_text(expected_text)

    def verify_account_created_title_text(self, expected_text: str):
        expect(self.account_created_title).to_have_text(expected_text)

    def verify_account_deleted_title_text(self, expected_text: str):
        expect(self.account_deleted_title).to_have_text(expected_text)

    def click_continue(self):
        self.continue_button.click()