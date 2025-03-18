import re
from playwright.sync_api import Page, expect

def test_switcher_main_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/")

    page.get_by_role("button", name="Укр ").click()
    page.get_by_role("link", name="Рус").click()

    # Перевірка ереходу ыз укр версыъ на ру та зміна заголовка Н1.
    expect(page).to_have_title(re.compile("Техническое обслуживание и ремонт автомобилей – доступная цена | СТО OILER"))
