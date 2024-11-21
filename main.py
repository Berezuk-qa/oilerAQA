import pytest
import re
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не нужен видимый браузер
        yield browser
        browser.close()


def test_zapus_na_servis_ua(browser):
    page = browser.new_page()

    try:
        # Открытие целевой страницы
        page.goto("https://oiler.pro/ua-ua/tehnicheskij-tovar/")

        # Нажатие кнопки "Купити"
        page.get_by_role("button", name="Купити").click()

        # Нажатие "Оформити замовлення"
        page.locator("#ui-id-4").get_by_role("button", name="Оформити замовлення").click()

        # Переход к форме оформления
        page.goto("https://oiler.pro/ua-ua/checkout/#step-phone")

        # Заполнение телефона
        phone_input = page.get_by_placeholder("Мобільний телефон")
        phone_input.click()
        phone_input.fill("+38 095 681 05 44")
        page.locator("div").filter(has_text="Особистий кабінет Закрити Особистий кабінет Електронна пошта Пароль Особистий ка").nth(2).click()
        # Переход к выбору доставки
        page.get_by_role("button", name="Доставка та оплата").click()
        page.get_by_role("row", name="Oiler Відрадний").get_by_role("cell").first.click()

        # Заполнение комментария
        comment_input = page.get_by_placeholder("Коментар")
        comment_input.click()
        comment_input.fill("TEST * Записатись на автосервіс * Відрадний")

        # Переход на следующий шаг
        page.get_by_role("button", name="Наступне").click()

        # Размещение заказа
        page.get_by_role("button", name="Розмістити Замовлення").click()

        # Проверка заголовка страницы
        expect(page).to_have_title(re.compile("Success Page"))

        # Альтернативная проверка наличия текста "Дякуємо"
        success_text = page.locator("text=Дякуємо")
        assert success_text.is_visible(), 'Текст "Дякуємо" не найден на странице.'

    finally:
        # Закрытие страницы в конце теста
        page.close()
