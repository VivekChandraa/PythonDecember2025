import time

from playwright.sync_api import Page


def test_placeholder(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_role("button",name="Hide").click()
    page.get_by_placeholder("Hide/Show Example").is_hidden()
    page.get_by_role("button", name="Show").click()
    page.get_by_placeholder("Hide/Show Example").is_visible()
    page.get_by_placeholder("Hide/Show Example").fill("Vivek Chandra")
    time.sleep(6)