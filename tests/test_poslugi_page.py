import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


def test_wiget_sto_ua(browser):
    page = browser.new_page()
    page.goto("https://oiler.pro/ua-ua/sto/")

    # Перевіряєм наявність заголовків віджетів на строрінці
    assert page.is_visible("text=СТО в Києві - OILER"), 'Текст "СТО в Києві - OILER" не знайдено на сторінці.'
    assert page.is_visible("text=Ціни на послуги"), 'Текст "Ціни на послуги" не знайдено на сторінці.'
    assert page.is_visible("text=Станом на сьогодні ми обслуговуємо"), 'Станом на сьогодні ми обслуговуємо" не знайдено на сторінці.'
    assert page.is_visible("text=Причини обрати Oiler"), 'Текст "Причини обрати Oiler" не знайдено на сторінці.'
    assert page.is_visible("text=Схема нашої роботи"), 'Текст "Схема нашої роботи" не знайдено на сторінці.'
    assert page.is_visible("text=Відгуки клієнтів"), 'Текст "Відгуки клієнтів" не знайдено на сторінці.'
    assert page.is_visible("text=Ми обслуговуємо"), 'Текст "Ми обслуговуємо" не знайдено на сторінці.'
    assert page.is_visible("text=Ремонт автомобіля"), 'Текст "Ремонт автомобіля" не знайдено на сторінці.'
    assert page.is_visible("text=Питання та відповіді"), 'Текст "Питання та відповіді" не знайдено на сторінці.'
    page.close()

def test_wiget_sto_ru(browser):
    page = browser.new_page()
    page.goto("https://oiler.pro/ua-ru/sto/")

    # Перевіряєм наявність заголовків віджетів на строрінці
    assert page.is_visible("text=СТО в Киеве - OILER"), 'Текст "СТО в Киеве - OILER" не знайдено на сторінці.'
    assert page.is_visible("text=Цены на услуги"), 'Текст "Цены на услуги" не знайдено на сторінці.'
    assert page.is_visible("text=По состоянию на сегодня мы обслуживаем"), 'По состоянию на сегодня мы обслуживаем" не знайдено на сторінці.'
    assert page.is_visible("text=Причины выбрать Oiler"), 'Текст "Причины выбрать Oiler" не знайдено на сторінці.'
    assert page.is_visible("text=Схема нашей работы"), 'Текст "Схема нашей работы" не знайдено на сторінці.'
    assert page.is_visible("text=Отзывы клиентов"), 'Текст "Отзывы клиентов" не знайдено на сторінці.'
    assert page.is_visible("text=Мы обслуживаем"), 'Текст "Мы обслуживаем" не знайдено на сторінці.'
    assert page.is_visible("text=Ремонт автомобиля"), 'Текст "Ремонт автомобиля" не знайдено на сторінці.'
    assert page.is_visible("text=Вопросы и ответы"), 'Текст "Вопросы и ответы" не знайдено на сторінці.'
    page.close()


def test_click_bmw_service_sto_ua(browser):
    page = browser.new_page()

    # Открываем целевую страницу
    page.goto("https://oiler.pro/ua-ua/sto/")

    # Находим элемент и кликаем на него
    bmw_element = page.locator('[title="СТО для BMW"]')
    bmw_element.click()

    # Проверяем, что URL изменился на ожидаемый
    expected_url = "https://oiler.pro/ua-ua/sto/sto-dlya-bmw/"  # Убедитесь, что это правильный URL
    #page.wait_for_url(expected_url, timeout=50000)  # Ждем, пока страница загрузится

    assert page.url == expected_url, f"Expected URL to be {expected_url}, but got {page.url}"

    # Закрываем страницу
    page.close()


def test_click_bmw_service_sto_ru(browser):
    page = browser.new_page()

    # Открываем целевую страницу
    page.goto("https://oiler.pro/ua-ru/sto/")

    # Находим элемент и кликаем на него
    bmw_element = page.locator('[title="СТО для BMW"]')
    bmw_element.click()

    # Проверяем, что URL изменился на ожидаемый
    expected_url = "https://oiler.pro/ua-ru/sto/sto-dlya-bmw/"  # Убедитесь, что это правильный URL
    #page.wait_for_url(expected_url, timeout=50000)  # Ждем, пока страница загрузится

    assert page.url == expected_url, f"Expected URL to be {expected_url}, but got {page.url}"

    # Закрываем страницу
    page.close()