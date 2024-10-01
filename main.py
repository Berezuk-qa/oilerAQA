from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oiler.pro/ua-ua/")
    page.get_by_placeholder("Пошук").click()
    page.get_by_placeholder("Пошук").fill("Технічний товар")
    page.get_by_placeholder("Пошук").press("Enter")

    context.close()
    browser.close()
