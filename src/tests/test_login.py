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

    (
        home_page
        .accept_cookies_if_present()
        .click_login_dropdown()
        .click_login_hudl()
    )
    (
        login_page
        .enter_email(valid_email)
        .tap_continue_button()
        .enter_password(valid_password)
        .tap_continue_button()
    )
    (
        home_page
        .close_tooltip_if_present()
        .verify_user_dropdown_present()
    )


@pytest.mark.p0
@pytest.mark.regression
def test_edit_wrong_password_to_correct_one_and_login(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    driver.get(base_url)

    (
        home_page
        .accept_cookies_if_present()
        .click_login_dropdown()
        .click_login_hudl()
    )
    (
        login_page
        .enter_email(valid_email)
        .tap_continue_button()
        .enter_password(wrong_password)
        .tap_continue_button()
        .verify_incorrect_credentials_message_present()
        .verify_error_icon_present()
        .enter_password(valid_password)
        .tap_continue_button()
    )
    (
        home_page
        .close_tooltip_if_present()
        .verify_user_dropdown_present()
    )


@pytest.mark.p1
@pytest.mark.regression
def test_login_page_elements_present(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    driver.get(base_url)

    (
        home_page
        .reject_cookies_if_present()
        .click_login_dropdown()
        .click_login_hudl()
    )
    (
        login_page
        .verify_hudl_logo_present()
        .verify_email_input_field_present()
        .verify_email_placeholder_present()
        .verify_continue_with_google_present()
        .verify_continue_with_facebook_present()
        .verify_dont_have_account_text_present()
        .verify_create_account_link_present()
        .verify_footer_text()
        .verify_privacy_policy_link()
        .verify_terms_of_service_link()
    )


@pytest.mark.p2
@pytest.mark.regression
def test_edit_wrong_email_and_password_to_valid_and_login(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    driver.get(base_url)

    (
        home_page
        .accept_cookies_if_present()
        .click_login_dropdown()
        .click_login_hudl()
    )
    (
        login_page
        .enter_email(wrong_email)
        .tap_continue_button()
        .enter_password(wrong_password)
        .tap_continue_button()
        .verify_incorrect_username_or_password_message_present()
        .verify_error_icon_present()
        .clear_and_enter_email(valid_email)
        .tap_continue_button()
        .enter_password(valid_password)
        .tap_continue_button()
    )
    (
        home_page
        .close_tooltip_if_present()
        .verify_user_dropdown_present()
    )


@pytest.mark.p3
@pytest.mark.regression
def test_invalid_email_format_handling(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    driver.get(base_url)

    (
        home_page
        .click_login_dropdown()
        .click_login_hudl()
    )
    (
        login_page
        .enter_email(invalid_email)
        .tap_continue_button()
        .verify_invalid_email_message_present()
        .verify_error_icon_present()
    )
