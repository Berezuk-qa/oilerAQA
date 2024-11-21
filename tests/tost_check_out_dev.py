import pytest, re
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

with open('filename.txt', 'w', encoding='utf-8') as f:
    f.write(data)

def test_dev_zapus_na_servis_ru(browser):
    page = browser.new_page()
    page.goto("https://dev.oiler.ua/ua-ru/tehnicheskij-tovar/")
    page.get_by_role("button", name="Купить").click()
    page.locator("#ui-id-4").get_by_role("button", name="Оформить заказ").click()
    page.goto("https://dev.oiler.ua/ua-ru/checkout/#step-phone")
    page.get_by_placeholder("Мобильный телефон").click()
    page.get_by_placeholder("Мобильный телефон").fill("+38 095 681 05 44")
    page.get_by_role("button", name="Доставка и оплата").click()
    page.get_by_role("row", name="Oiler Отрадный").get_by_role("cell").first.click()
    page.get_by_role("row", name="Записаться на автосервис").locator("div").click()
    page.get_by_placeholder("Комментарий").click()
    page.get_by_placeholder("Комментарий").fill("Записаться на автосервис * Oiler Отрадный")
    page.get_by_role("button", name="Следующий").click()
    page.get_by_role("button", name="Оформить заказ").click()
    expect(page).to_have_title(re.compile("Success Page"))
    #assert page.is_visible(timeout=5000)"text=Дякуємо"), 'Текст "Дякуємо" не знайдено на сторінці.'
    #page.locator(".cl-dialog-close-icon > img").click()
    page.close()

with open('filename.txt', 'w', encoding='utf-8') as f:
    f.write(data)

def test_dev_samoviviz_ru(browser):
    page = browser.new_page()
    page.goto("https://dev.oiler.ua/ua-ru/tehnicheskij-tovar/")
    page.locator("#product_addtocart_form div").filter(has_text="Купить").nth(2).click()
    page.get_by_role("button", name="Купить").click()
    page.locator("#ui-id-4").get_by_role("button", name="Оформить заказ").click()
    page.goto("https://dev.oiler.ua/ua-ru/checkout/#step-phone")
    page.get_by_placeholder("Мобильный телефон").click()
    page.get_by_placeholder("Мобильный телефон").fill("+38 095 681 05 44")
    page.get_by_role("button", name="Доставка и оплата").click()
    page.get_by_role("row", name="Самовывоз").get_by_role("cell").first.click()
    page.get_by_role("row", name="Oiler Демеевка").get_by_role("cell").first.click()
    page.get_by_placeholder("Комментарий").click()
    page.get_by_placeholder("Комментарий").fill("Самовывоз * Oiler Демеевка")
    page.get_by_role("button", name="Следующий").click()
    page.locator("label").filter(has_text="Наличными или картой на сервисе").click()
    page.get_by_role("button", name="Оформить заказ").click()
    expect(page).to_have_title(re.compile("Success Page"))
    page.close()


def test_dev_dostavka_kererom_ru(browser):
    page = browser.new_page()
    page.goto("https://dev.oiler.ua/ua-ru/tehnicheskij-tovar/")
    page.locator("#product_addtocart_form div").filter(has_text="Купить").nth(2).click()
    page.get_by_role("link", name="Корзина 1 1 items").click()
    page.get_by_role("button", name="Оформить заказ").click()
    page.goto("https://dev.oiler.ua/ua-ru/checkout/#step-phone")
    page.get_by_placeholder("Мобильный телефон").click()
    page.get_by_placeholder("Мобильный телефон").fill("+38 095 681 05 44")
    page.get_by_role("button", name="Доставка и оплата").click()
    page.get_by_role("row", name="Доставка курьером по Киеву -").get_by_role("cell").first.click()
    page.get_by_placeholder("Имя и фамилия").click()
    page.get_by_placeholder("Имя и фамилия").fill("Игорь")
    page.get_by_placeholder("Улица", exact=True).click()
    page.get_by_placeholder("Улица", exact=True).fill("Хрещатик")
    page.get_by_placeholder("Дом", exact=True).click()
    page.get_by_placeholder("Дом", exact=True).fill("1")
    page.get_by_placeholder("Комментарий").click()
    page.get_by_placeholder("Комментарий").fill("Доставка курьером по Киеву * Игорь Хрещатик 1")
    page.get_by_role("button", name="Следующий").click()
    page.locator("label").filter(has_text="Наличными курьеру при получении товара").click()
    page.get_by_role("button", name="Оформить заказ").click()
    expect(page).to_have_title(re.compile("Success Page"))
    page.close()

def test_dev_zapus_na_servis_ua(browser):
    page = browser.new_page()
    page.goto("https://dev.oiler.ua/ua-ua/tehnicheskij-tovar/")
    page.get_by_role("button", name="Купити").click()
    page.locator("#ui-id-4").get_by_role("button", name="Оформити замовлення").click()
    page.goto("https://dev.oiler.ua/ua-ua/checkout/#step-phone")
    page.get_by_placeholder("Мобільний телефон").click()
    page.get_by_placeholder("Мобільний телефон").fill("+38 095 681 05 44")
    page.get_by_role("button", name="Доставка та оплата").click()
    page.get_by_role("row", name="Oiler Відрадний").get_by_role("cell").first.click()
    page.get_by_placeholder("Коментар").click()
    page.get_by_placeholder("Коментар").fill("TEST * Записатись на автосервіс * Відрадний")
    page.get_by_role("button", name="Наступне").click()
    page.get_by_role("button", name="Розмістити Замовлення").click()
    expect(page).to_have_title(re.compile("Success Page"))
    #assert page.is_visible(timeout=5000)"text=Дякуємо"), 'Текст "Дякуємо" не знайдено на сторінці.'
    page.close()


def test_dev_samoviviz_ua(browser):
    page = browser.new_page()
    page.goto("https://dev.oiler.ua/ua-ua/tehnicheskij-tovar/")
    page.locator(".cl-dialog-close-icon > img").click()
    page.get_by_role("button", name="Купити").click()
    page.locator("#ui-id-4").get_by_role("button", name="Оформити замовлення").click()
    page.goto("https://dev.oiler.ua/ua-ua/checkout/#step-phone")
    page.get_by_placeholder("Мобільний телефон").click()
    page.get_by_placeholder("Мобільний телефон").fill("+38 095 681 05 44")
    page.get_by_role("button", name="Доставка та оплата").click()
    page.get_by_role("row", name="Самовивіз").get_by_role("cell").first.click()
    page.get_by_role("row", name="Oiler Троєщина").get_by_role("cell").first.click()
    page.get_by_placeholder("Коментар").click()
    page.get_by_placeholder("Коментар").fill("TEST * Самовивіз * Троєщина")
    page.get_by_role("button", name="Наступне").click()
    page.locator("label").filter(has_text="Готівкою або карткою на сервісі").click()
    page.get_by_role("button", name="Розмістити Замовлення").click()
    expect(page).to_have_title(re.compile("Success Page"))
    page.close()


def test_dev_dostavka_kererom_ua(browser):
    page = browser.new_page()
    page.goto("https://dev.oiler.ua/ua-ua/tehnicheskij-tovar/")
    page.get_by_role("button", name="Купити").click()
    page.locator("#ui-id-4").get_by_role("button", name="Оформити замовлення").click()
    page.goto("https://dev.oiler.ua/ua-ua/checkout/#step-phone")
    page.get_by_placeholder("Мобільний телефон").click()
    page.get_by_placeholder("Мобільний телефон").fill("+38 095 681 05 44")
    page.get_by_role("button", name="Доставка та оплата").click()
    page.get_by_role("row", name="Доставка кур’єром по Києву -").get_by_role("cell").first.click()
    page.get_by_placeholder("Ім’я та прізвище").click()
    page.get_by_placeholder("Ім’я та прізвище").fill("ТЕСТ")
    page.get_by_placeholder("Вулиця", exact=True).click()
    page.get_by_placeholder("Вулиця", exact=True).fill("хрещатик")
    page.get_by_placeholder("Будинок").click()
    page.get_by_placeholder("Будинок").fill("1")
    page.get_by_placeholder("Коментар").click()
    page.get_by_placeholder("Коментар").fill("TEST * Доставка кур’єром по Києву")
    page.get_by_role("button", name="Наступне").click()
    page.locator("label").filter(has_text="Готівкою кур'єру при отриманні товару").click()
    page.get_by_role("button", name="Розмістити Замовлення").click()
    expect(page).to_have_title(re.compile("Success Page"))
    page.close()


