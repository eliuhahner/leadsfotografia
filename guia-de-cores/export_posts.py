import asyncio
from playwright.async_api import async_playwright
import os

async def export_posts():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        html_path = os.path.abspath(".")
        
        post_configs = [
            {"file": "post_bastidores.html", "id": "post-bastidores", "name": "post_bastidores.png"},
            {"file": "post_depoimento.html", "id": "post-depoimento", "name": "post_depoimento.png"},
            {"file": "post_foto_cabeceira.html", "id": "post-foto-cabeceira", "name": "post_foto_cabeceira.png"},
            {"file": "post_urgencia.html", "id": "post-urgencia", "name": "post_urgencia.png"},
            {"file": "post_4dias.html", "id": "post-4dias", "name": "post_4dias.png"},
        ]
        
        for config in post_configs:
            print(f"Exporting {config['name']}...")
            
            file_url = f"file:///{os.path.join(html_path, config['file'])}"
            
            page = await browser.new_page(viewport={"width": 1080, "height": 1350})
            await page.goto(file_url, wait_until="networkidle")
            
            # Wait for fonts to load
            await page.wait_for_timeout(2000)
            
            # Find the post element
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
        print("\nAll posts exported!")

asyncio.run(export_posts())