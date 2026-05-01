import asyncio
from playwright.async_api import async_playwright
import os

async def export_slides():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        html_path = os.path.abspath("carousel.html")
        file_url = f"file:///{html_path}"
        
        slide_configs = [
            {"id": "slide-1", "name": "01_hook.png"},
            {"id": "slide-2", "name": "02_problema.png"},
            {"id": "slide-3", "name": "03_solucao.png"},
            {"id": "slide-4", "name": "04_beneficio1.png"},
            {"id": "slide-5", "name": "05_beneficio2.png"},
            {"id": "slide-6", "name": "06_beneficio3.png"},
            {"id": "slide-7", "name": "07_prova_social.png"},
            {"id": "slide-8", "name": "08_cta.png"},
        ]
        
        for config in slide_configs:
            print(f"Exporting {config['name']}...")
            
            page = await browser.new_page(viewport={"width": 1080, "height": 1350})
            await page.goto(file_url, wait_until="networkidle")
            
            # Wait for fonts to load
            await page.wait_for_timeout(2000)
            
            # Find the slide element
            element = await page.query_selector(f"#{config['id']}")
            
            if element:
                # Scroll element into view
                await element.scroll_into_view_if_needed()
                await page.wait_for_timeout(500)
                
                # Take screenshot of the element
                await element.screenshot(path=config['name'], type="png")
                print(f"  -> {config['name']} exported successfully")
            else:
                print(f"  -> ERROR: Could not find {config['id']}")
            
            await page.close()
        
        await browser.close()
        print("\nAll slides exported!")

asyncio.run(export_slides())