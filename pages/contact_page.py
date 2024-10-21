from playwright.sync_api import Page, expect

class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.contact_form_heading = page.locator('h2.title.text-center', has_text="Get In Touch")
        self.contact_name_input = page.locator('[data-qa="name"]')
        self.contact_email_input = page.locator('[data-qa="email"]')
        self.contact_subject_input = page.locator('[data-qa="subject"]')
        self.contact_message_textarea = page.locator('[data-qa="message"]')
        self.contact_file_upload = page.locator('input[type="file"]')
        self.submit_button = page.locator('[data-qa="submit-button"]')
        self.success_message = page.locator('.status.alert.alert-success')
        self.feedback_heading = page.locator('h2.title.text-center', has_text="Feedback For Us")
        self.home_button = page.locator('a.btn.btn-success') 

    def goto(self):
        self.page.goto('https://automationexercise.com/contact_us')

    def fill_contact_form(self, name: str, email: str, subject: str, message: str):
        self.contact_name_input.fill(name)
        self.contact_email_input.fill(email)
        self.contact_subject_input.fill(subject)
        self.contact_message_textarea.fill(message)

    def upload_file(self, file_path: str):
        self.contact_file_upload.set_input_files(file_path)

    def submit_contact_form(self):
        self.submit_button.click()

    def verify_success_message(self, expected_text: str):
        expect(self.success_message).to_be_visible()
        expect(self.success_message).to_have_text(expected_text)

    def verify_feedback_section(self):
        expect(self.feedback_heading).to_be_visible()

    def click_submit_button(self):
        self.submit_button.click()

    def click_home_button(self):
        self.home_button.click()
