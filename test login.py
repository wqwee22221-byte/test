import re

import pytest
from playwright.sync_api import Page, expect

LOGIN_URL = "https://onlypult.com/login"

# Selectors below are shared across login test cases in this file - reuse them
# instead of duplicating raw CSS when adding new cases.
EMAIL_INPUT = ".field-loginform-email input"
PASSWORD_INPUT = ".input-group.input-group-lg input"
LOGIN_BUTTON = ".btn.btn-primary.btn-lg.btn-block.mb-3"
PASSWORD_FIELD_ERROR = ".field-loginform-password .help-block"
CAPTCHA_V3_INPUT = "#loginform-captchav3"

INVALID_EMAIL = "zxczxczxc123123123123@asd.com"
VALID_LENGTH_PASSWORD = "Test123!"

INCORRECT_CREDENTIALS_ERROR = "Sorry, incorrect e-mail or password."


@pytest.fixture
def login_page(page: Page) -> Page:
    page.goto(LOGIN_URL)
    return page


def test_case_1_invalid_email_for_login(login_page: Page):
    login_page.locator(EMAIL_INPUT).fill(INVALID_EMAIL)
    login_page.locator(PASSWORD_INPUT).fill(VALID_LENGTH_PASSWORD)

    # The form is gated by an invisible reCAPTCHA v3 token that populates
    # this hidden field asynchronously after page load; clicking Login
    # before it's ready leaves the button disabled and submits nothing.
    expect(login_page.locator(CAPTCHA_V3_INPUT)).not_to_have_value("")

    login_page.locator(LOGIN_BUTTON).click()

    expect(login_page).to_have_url(re.compile(r"onlypult\.com/login"))
    expect(login_page.locator(PASSWORD_FIELD_ERROR)).to_have_text(INCORRECT_CREDENTIALS_ERROR)
