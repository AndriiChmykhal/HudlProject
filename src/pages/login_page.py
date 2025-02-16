from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    accept_cookies = (By.ID, "onetrust-accept-btn-handler")
    login_dropdown = (By.CSS_SELECTOR, "[data-qa-id='login-select']")
    login_hudl = (By.CSS_SELECTOR, "[data-qa-id='login-hudl']")
    email_input = (By.NAME, "username")
    password_input = (By.ID, "password")
    continue_button = (By.CSS_SELECTOR, "button[type='submit']")
    error_message = (By.CLASS_NAME, "ulp-input-error-message")
    error_icon = (By.CLASS_NAME, "ulp-input-error-icon")
    edit_email = (By.CSS_SELECTOR, "a[data-link-name='edit-username']")
    show_password = (By.CSS_SELECTOR, "button[data-action='toggle']")
    email_placeholder = (By.CSS_SELECTOR, "label[for='username']")
    hudl_logo = (By.ID, "custom-prompt-logo")
    login_title = (By.XPATH, "//h1[text()='Log In']")
    continue_with_google = (By.CSS_SELECTOR, "button[data-provider='google']")
    continue_with_google = (By.CSS_SELECTOR, "button[data-provider='facebook']")

    def enter_email(self, email):
        self.wait.until(ec.visibility_of_element_located(self.email_input)).send_keys(email)

    def enter_password(self, password):
        self.wait.until(ec.visibility_of_element_located(self.password_input)).send_keys(password)

    def tap_continue_button(self):
        self.wait.until(ec.element_to_be_clickable(self.continue_button)).click()

    def verify_error_message_present(self):
        assert self.wait.until(ec.presence_of_element_located(self.error_message))

    def verify_error_icon_present(self):
        assert self.wait.until(ec.presence_of_element_located(self.error_icon))

    def click_edit_email(self):
        self.wait.until(ec.element_to_be_clickable(self.edit_email)).click()

    def clear_and_enter_email(self, new_email):
        self.click_edit_email()
        email_field = self.wait.until(ec.element_to_be_clickable(self.email_input))
        email_field.click()
        email_field.send_keys(Keys.COMMAND + "a")  # for Mac
        email_field.send_keys(Keys.DELETE)
        email_field.send_keys(new_email)

    def verify_email_placeholder_present(self):
        assert self.wait.until(
            ec.presence_of_element_located(self.email_placeholder)), "Email* placeholder is absent in input field"

    def verify_hudl_logo_present(self):
        assert self.wait.until(
            ec.presence_of_element_located(self.hudl_logo)), "Hudl logo is absent"

    def verify_continue_with_google_present(self):
        assert self.wait.until(
            ec.presence_of_element_located(self.continue_with_google)), "Continue with Google button is absent"

    def verify_continue_with_facebook_present(self):
        assert self.wait.until(
            ec.presence_of_element_located(self.continue_with_google)), "Continue with Facebook button is absent"

    def verify_email_input_filed_present(self):
        assert self.wait.until(
            ec.presence_of_element_located(self.email_input)), "Email input field is absent"



