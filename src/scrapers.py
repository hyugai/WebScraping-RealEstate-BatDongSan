# libs
from usr_lib import *

async def scrape_pages_hrefs(
        url: str) -> None: 
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=UserAgent().random) 
        page = await context.new_page()

        await page.goto(url)
        title = await page.title()

        print(title)
