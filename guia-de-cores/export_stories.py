import asyncio
from playwright.async_api import async_playwright
import os

async def export_stories():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        html_path = os.path.abspath("stories.html")
        file_url = f"file:///{html_path}"
        
        story_configs = [
            {"id": "story-1", "name": "story_01_hook.png"},
            {"id": "story-2", "name": "story_02_problema.png"},
            {"id": "story-3", "name": "story_03_solucao.png"},
            {"id": "story-4", "name": "story_04_beneficio1.png"},
            {"id": "story-5", "name": "story_05_beneficio2.png"},
            {"id": "story-6", "name": "story_06_beneficio3.png"},
            {"id": "story-7", "name": "story_07_agenda_aberta.png"},
            {"id": "story-8", "name": "story_08_cta.png"},
        ]
        
        for config in story_configs:
            print(f"Exporting {config['name']}...")
            
            page = await browser.new_page(viewport={"width": 1080, "height": 1920})
            await page.goto(file_url, wait_until="networkidle")
            
            # Wait for fonts to load
            await page.wait_for_timeout(2000)
            
            # Find the story element
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
        print("\nAll stories exported!")

asyncio.run(export_stories())