# libs
from libs import *

# URLScrapper
class URLScrapper():
    async def sellingTypesURLs_collector(self, 
                                         p: Playwright) -> None:
        browser = await p.chromium.launch(headless=False) 
        context = await browser.new_context(user_agent=UserAgent().random)
        page = await context.new_page()
        await page.goto(HOMEPAGE, wait_until='domcontentloaded')

        realEstate_forSale_xpath = "//a[text()='Bất động sản bán']/parent::div/following-sibling::ul" 
        # apartments
        xpath = realEstate_forSale_xpath + "/descendant::a[text()='Bán căn hộ chung cư']/parent::div/following-sibling::ul/descendant::a" 
        nodes_ul = await page.locator(selector=f'xpath={xpath}').all()

        await browser.close()
    
    async def extract(self):
        async with async_playwright() as p:
            await self.sellingTypesURLs_collector(p) 

    def main(self):
        asyncio.run(self.extract())