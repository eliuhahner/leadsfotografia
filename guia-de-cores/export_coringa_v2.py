import asyncio
from playwright.async_api import async_playwright
import os

async def export_coringa_v2():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        html_path = os.path.abspath("post_coringa_v2.html")
        file_url = f"file:///{html_path}"
        
        slide_configs = [
            {"id": "coringa-v2-1", "name": "coringa_v2_01_hook.png"},
            {"id": "coringa-v2-2", "name": "coringa_v2_02_problema.png"},
            {"id": "coringa-v2-3", "name": "coringa_v2_03_beneficios.png"},
            {"id": "coringa-v2-4", "name": "coringa_v2_04_cta.png"},
        ]
        
        for config in slide_configs:
            print(f"Exporting {config['name']}...")
            
            page = await browser.new_page(viewport={"width": 1080, "height": 1350})
            await page.goto(file_url, wait_until="networkidle")
            await page.wait_for_timeout(2000)
            
            element = await page.query_selector(f"#{config['id']}")
            
            if element:
                await element.scroll_into_view_if_needed()
                await page.wait_for_timeout(500)
                await element.screenshot(path=config['name'], type="png")
                print(f"  -> {config['name']} exported successfully")
            else:
                print(f"  -> ERROR: Could not find {config['id']}")
            
            await page.close()
        
        await browser.close()
        print("\nAll coringa v2 slides exported!")

if __name__ == "__main__":
    asyncio.run(export_coringa_v2())
