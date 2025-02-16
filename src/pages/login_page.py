from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from utils.config import terms_of_service_url, privacy_policy_url


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
    continue_with_facebook = (By.CSS_SELECTOR, "button[data-provider='facebook']")
    continue_with_apple = (By.CSS_SELECTOR, "button[data-provider='apple']")
    dont_have_account_text = (By.XPATH, "//p[contains(text(), \"Don't have an account?\")]")
    create_account_link = (By.XPATH, "//a[contains(text(), 'Create Account')]")
    footer_text_locator = (By.XPATH, "//footer[contains(text(), 'By continuing, you agree to our')]")
    privacy_policy_link_locator = (By.XPATH, "//footer//a[contains(text(), 'Privacy Policy')]")
    terms_of_service_link_locator = (By.XPATH, "//footer//a[contains(text(), 'Terms of Service')]")
    footer_full_text_locator = (By.XPATH, "//footer")

    privacy_policy_link_locator = (By.XPATH, "//footer//a[contains(text(), 'Privacy Policy')]")
    terms_of_service_link_locator = (By.XPATH, "//footer//a[contains(text(), 'Terms of Service')]")

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

    def verify_email_input_filed_present(self):
        assert self.wait.until(
            ec.presence_of_element_located(self.email_input)), "Email input field is absent"

    def verify_continue_with_google_present(self):
        assert self.wait.until(
            ec.presence_of_element_located(self.continue_with_google)), "Continue with Google button is absent"

    def verify_continue_with_facebook_present(self):
        assert self.wait.until(
            ec.presence_of_element_located(self.continue_with_google)), "Continue with Facebook button is absent"

    def verify_continue_with_apple_present(self):
        assert self.wait.until(
            ec.presence_of_element_located(self.continue_with_apple)), "Continue with Apple button is absent"

    def verify_dont_have_account_text_present(self):
        assert self.wait.until(ec.presence_of_element_located(self.dont_have_account_text))

    def create_account_link_present(self):
        assert self.wait.until(ec.presence_of_element_located(self.create_account_link))

    def verify_footer_text(self):
        footer_element = self.wait.until(ec.presence_of_element_located(self.footer_full_text_locator))
        footer_text = footer_element.text.strip()
        expected_text = "By continuing, you agree to our Privacy Policy and Terms of Service"

        assert footer_text == expected_text, f"Footer text is incorrect! Found: '{footer_text}'"

    def verify_privacy_policy_link(self):
        privacy_link = self.wait.until(ec.presence_of_element_located(self.privacy_policy_link_locator))
        assert privacy_link.text == "Privacy Policy", "Privacy Policy text is incorrect!"
        assert privacy_link.get_attribute(
            "href") == privacy_policy_url, "Privacy Policy link is incorrect!"

    def verify_terms_of_service_link(self):
        terms_link = self.wait.until(ec.presence_of_element_located(self.terms_of_service_link_locator))
        assert terms_link.text == "Terms of Service", "Terms of Service text is incorrect!"
        assert terms_link.get_attribute("href") == terms_of_service_url, "Terms of Service link is incorrect!"
