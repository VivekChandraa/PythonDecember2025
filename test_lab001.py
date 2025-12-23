from playwright.sync_api import Page #calling Page class

def test_lab001(playwright): #initiate browser method 2
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.udemy.com")

def test_lab002(page: Page): #initiate browser method 2
    page.goto("https://www.udemy.com")