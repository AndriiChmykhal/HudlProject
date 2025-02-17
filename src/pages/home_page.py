from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time



class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.actions = ActionChains(driver)

    accept_all_cookies = (By.ID, "onetrust-accept-btn-handler")
    reject_cookies = (By.ID, "onetrust-reject-all-handler")
    login_dropdown = (By.CSS_SELECTOR, "[data-qa-id='login-select']")
    login_hudl = (By.CSS_SELECTOR, "[data-qa-id='login-hudl']")
    logo_hudl = (By.CSS_SELECTOR, "[data-qa-id='site-logo']")
    tool_tip = (By.CLASS_NAME, "uni-tooltip-custom")
    close_icon_tool_tip = (By.CLASS_NAME, "u-onboarding-custom__dismiss")
    user_logged_in_drop_down = (By.CLASS_NAME, "hui-globaluseritem__display-name")

    def accept_cookies_if_present(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            accept_cookie_button = wait.until(ec.element_to_be_clickable(self.accept_all_cookies))
            accept_cookie_button.click()
        except TimeoutException:
            print("Cookies accept button not found or not clickable.")

    def reject_cookies_if_present(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            reject_cookie_button = wait.until(ec.element_to_be_clickable(self.reject_cookies))
            reject_cookie_button.click()
        except TimeoutException:
            print("Reject accept button not found or not clickable.")

    def click_login_dropdown(self):
        self.wait.until(ec.element_to_be_clickable(self.login_dropdown)).click()

    def click_login_hudl(self):
        self.wait.until(ec.element_to_be_clickable(self.login_hudl)).click()

    def close_tooltip_if_present(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.tool_tip))
            self.wait.until(ec.element_to_be_clickable(self.close_icon_tool_tip)).click()
        except:
            pass

    def verify_user_dropdown_present(self):
        assert self.wait.until(ec.presence_of_element_located(self.user_logged_in_drop_down))
