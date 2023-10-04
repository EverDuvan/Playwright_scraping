import re
import time
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://farmacialabomba.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://farmacialabomba.com/")
    time.sleep(10)

    # Click the get started link.
    page.get_by_role("checkbox", name="Verify tou are human").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    browser.close()