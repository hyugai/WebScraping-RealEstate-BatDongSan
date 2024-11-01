# libs
from libs import *

# URLScrapper
class URLScrapper():
    async def sellingTypesURLs_collector(self, 
                                         p: Playwright) -> None:
        browser = await p.chromium.launch(headless=False) 
        context = await browser.new_context(user_agent=UserAgent().random)
        page = await context.new_page()
        await page.goto(HOMEPAGE, timeout=0, wait_until='domcontentloaded')
        title = await page.title()
        print(title)
        await page.screenshot(path='screenshot.png')

        await browser.close()
    
    async def extract(self):
        async with async_playwright() as p:
            await self.sellingTypesURLs_collector(p) 

    def main(self):
        asyncio.run(self.extract())