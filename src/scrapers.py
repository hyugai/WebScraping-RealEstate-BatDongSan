# libs
from usr_lib import *

def scrape_pages_hrefs(
        url: str) -> None: 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent=UserAgent().random)
        new_page = context.new_page()
        
        new_page.goto(url, wait_until="domcontentloaded")
        node_a = new_page.locator("xpath=//a[text()='Bất động sản bán']")  
        print(node_a)
#    async with async_playwright() as p:
#        browser = await p.chromium.launch(headless=False)
#        context = await browser.new_context(user_agent=UserAgent().random) 
#        page = await context.new_page()
#
#        await page.goto(url)
#        title = await page.title()
#
#        print(title)
