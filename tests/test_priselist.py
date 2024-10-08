import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


def test_price_list(browser):
    page = browser.new_page()
    page.goto("https://oiler.pro/ua-ua/sto/")

    # Открываем прайс-лист, нужно указать правильный селектор для кнопки/ссылки
    price_list_button = page.locator("text=Прайс-лист")  # замените на актуальный текст или селектор
    price_list_button.click()

    # Проверяем наличие текста в открывшемся прайс-листе
    assert page.is_visible("text=Ціни на послуги"), 'Текст "Ціни на послуги" не найден в прайс-листе.'

    page.close()
