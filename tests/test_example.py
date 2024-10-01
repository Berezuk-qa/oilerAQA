import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://oiler.pro/ua-ru/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Oiler"))

def test_get_started_link(page: Page):
    page.goto("https://oiler.pro/ua-ru/")

    # Перехід всі статті блог1у.
    page.get_by_role("link", name="Все статьи").click()

    # Перевірка чи є в назві слово Блог.
    expect(page.get_by_role("heading", name="Блог")).to_be_visible()
