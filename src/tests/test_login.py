import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config import base_url, valid_email, valid_password, wrong_email, wrong_password, invalid_email


@pytest.mark.p0
@pytest.mark.smoke
@pytest.mark.regression
def test_login_with_valid_credentials(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    driver.get(base_url)
    home_page.accept_cookies_if_present()
    home_page.click_login_dropdown()
    home_page.click_login_hudl()
    login_page.enter_email(valid_email)
    login_page.tap_continue_button()
    login_page.enter_password(valid_password)
    login_page.tap_continue_button()
    home_page.close_tooltip_if_present()
    home_page.verify_user_dropdown_present()


@pytest.mark.p0
@pytest.mark.regression
def test_edit_wrong_password_to_correct_one_and_login(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    driver.get(base_url)
    home_page.accept_cookies_if_present()
    home_page.click_login_dropdown()
    home_page.click_login_hudl()
    login_page.enter_email(valid_email)
    login_page.tap_continue_button()
    login_page.enter_password(wrong_password)
    login_page.tap_continue_button()
    login_page.verify_incorrect_credentials_message_present()
    login_page.verify_error_icon_present()
    login_page.enter_password(valid_password)
    login_page.tap_continue_button()
    home_page.close_tooltip_if_present()
    home_page.verify_user_dropdown_present()


@pytest.mark.p1
@pytest.mark.regression
def test_login_page_elements_present(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    driver.get(base_url)
    home_page.reject_cookies_if_present()
    home_page.click_login_dropdown()
    home_page.click_login_hudl()
    login_page.verify_hudl_logo_present()
    login_page.verify_email_input_filed_present()
    login_page.verify_email_placeholder_present()
    login_page.verify_continue_with_google_present()
    login_page.verify_continue_with_facebook_present()
    login_page.verify_dont_have_account_text_present()
    login_page.create_account_link_present()
    login_page.verify_footer_text()
    login_page.verify_privacy_policy_link()
    login_page.verify_terms_of_service_link()


@pytest.mark.p2
@pytest.mark.regression
def test_edit_wrong_email_and_password_to_valid_and_login(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    driver.get(base_url)
    home_page.accept_cookies_if_present()
    home_page.click_login_dropdown()
    home_page.click_login_hudl()
    login_page.enter_email(wrong_email)
    login_page.tap_continue_button()
    login_page.enter_password(wrong_password)
    login_page.tap_continue_button()
    login_page.verify_incorrect_username_or_password_message_present()
    login_page.verify_error_icon_present()
    login_page.clear_and_enter_email(valid_email)
    login_page.tap_continue_button()
    login_page.enter_password(valid_password)
    login_page.tap_continue_button()
    home_page.close_tooltip_if_present()
    home_page.verify_user_dropdown_present()


@pytest.mark.p3
@pytest.mark.regression
def test_invalid_email_format_handling(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    driver.get(base_url)
    home_page.click_login_dropdown()
    home_page.click_login_hudl()
    login_page.enter_email(invalid_email)
    login_page.tap_continue_button()
    login_page.verify_invalid_email_message_present()
    login_page.verify_error_icon_present()
