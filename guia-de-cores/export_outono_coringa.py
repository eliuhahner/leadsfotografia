import asyncio
from playwright.async_api import async_playwright
import os

async def export_outono_coringa():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        html_path = os.path.abspath("post_outono_coringa.html")
        file_url = f"file:///{html_path}"
        
        slide_configs = [
            {"id": "outono-1", "name": "outono_01_hook.png"},
            {"id": "outono-2", "name": "outono_02_risco.png"},
            {"id": "outono-3", "name": "outono_03_trato.png"},
            {"id": "outono-4", "name": "outono_04_duvida.png"},
            {"id": "outono-5", "name": "outono_05_cta.png"},
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
        print("\nAll outono coringa slides exported!")

if __name__ == "__main__":
    asyncio.run(export_outono_coringa())
