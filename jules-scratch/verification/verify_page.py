import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get the absolute path to the HTML file
        file_path = os.path.abspath('public/index.html')

        # Go to the local HTML file
        page.goto(f'file://{file_path}')

        # Take a screenshot
        page.screenshot(path='jules-scratch/verification/verification.png')

        browser.close()

run()