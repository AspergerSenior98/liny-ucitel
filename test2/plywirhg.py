from playwright.sync_api import sync_playwright
import os
with sync_playwright() as p:
    url = "https://souhrada.github.io/playwright-exam/"
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.fill("input#login", "Jarmil")
    page.fill("input#pass", "Admin123")
    page.click("button.login-btn")
    print(page.query_selector(".super-secret-text").inner_text())
    input("piš pro uzavreni")
    browser.close()