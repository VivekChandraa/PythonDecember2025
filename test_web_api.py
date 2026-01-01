from playwright.sync_api import Playwright


def test_web_apie2e(playwright: Playwright):
    browser =playwright.chromium.launch(headless=False)
    context =browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("vivekchandra@yopmail.com")
    page.get_by_placeholder("enter your passsword").fill("Vivek@123")
    page.locator("#login").click()
