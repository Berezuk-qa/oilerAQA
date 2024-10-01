import re
from playwright.sync_api import Page, expect

def test_ssearch_main_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/")
    page.get_by_placeholder("Пошук").fill("Технічний товар")
    page.get_by_placeholder("Пошук").press("Enter")

    # Перевірка відкриття сторінки пошуку
    expect(page).to_have_title(re.compile("Результати пошуку: 'Технічний товар'"))
