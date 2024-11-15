# Перевырка контенту на всіх типах сторінок
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

# код нижче переробити тестовий набір для перевірки контента на сторінках, чи є віджети
def test_price_list(browser):


    page = browser.new_page()
    page.goto("https://oiler.pro/ua-ua/sto/")

    # Открываем прайс-лист, нужно указать правильный селектор для кнопки/ссылки
    price_list_button = page.locator("text=Прайс-лист")  # замените на актуальный текст или селектор
    price_list_button.click()

    # Проверяем наличие текста в открывшемся прайс-листе
    assert page.is_visible("text=Ціни на послуги"), 'Текст "Ціни на послуги" не найден в прайс-листе.'

    page.close()