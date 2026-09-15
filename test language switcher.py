import re

import pytest
from playwright.sync_api import Page, expect

LOGIN_URL = "https://onlypult.com/login"

LANGUAGES = [
    ("Deutsch", "de", "de-DE", "Einloggen"),
    ("Español", "es", "es-ES", "Iniciar sesión"),
    ("Français", "fr", "fr-FR", "Se connecter"),
    ("Italiano", "it", "it-IT", "Accedi"),
    ("Português", "pt", "pt-PT", "Fazer login"),
]


@pytest.fixture
def login_page(page: Page) -> Page:
    page.goto(LOGIN_URL)
    return page


def test_default_language_is_english(login_page: Page):
    expect(login_page.locator("html")).to_have_attribute("lang", re.compile("^en"))
    expect(login_page.locator("h1")).to_have_text("Log in")


@pytest.mark.parametrize("link_text, url_slug, html_lang, heading_text", LANGUAGES)
def test_switching_language_changes_page_text(
    login_page: Page, link_text: str, url_slug: str, html_lang: str, heading_text: str
):
    login_page.locator(".languages-popover-link").click()
    login_page.locator(".popover").get_by_role("link", name=link_text, exact=True).click()

    expect(login_page).to_have_url(re.compile(rf"/{url_slug}/login$"))
    expect(login_page.locator("html")).to_have_attribute("lang", html_lang)
    expect(login_page.locator("h1")).to_have_text(heading_text)
