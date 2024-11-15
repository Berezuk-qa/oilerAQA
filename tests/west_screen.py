from playwright.sync_api import sync_playwright, Playwright

def main_ua(playwright: Playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oiler.pro/ua-ua/")
    page.screenshot(path="main_ua.png")
    browser.close()

with sync_playwright() as playwright:
    main_ua(playwright)

