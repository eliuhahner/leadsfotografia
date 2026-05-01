import asyncio
from playwright.async_api import async_playwright
import os

async def export_guia_premium():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # Caminho para o novo arquivo premium
        html_path = os.path.abspath("guia_cores_outono_premium.html")
        file_url = f"file:///{html_path}"
        
        output_name = "guia_cores_premium_final.png"
        
        print(f"Exportando {output_name}...")
        
        # Setup da página com o tamanho padrão do Instagram (Portrait)
        page = await browser.new_page(viewport={"width": 1080, "height": 1350})
        await page.goto(file_url, wait_until="networkidle")
        
        # Espera um pouco para garantir que as fontes e imagens carreguem e o backdrop-filter seja aplicado
        await page.wait_for_timeout(3000)
        
        # Seleciona o container principal
        element = await page.query_selector(".main-container")
        
        if element:
            await element.screenshot(path=output_name, type="png")
            print(f"  -> {output_name} exportado com sucesso!")
        else:
            print("  -> ERRO: Não foi possível encontrar o container .main-container")
        
        await browser.close()
        print("\nProcesso concluído!")

if __name__ == "__main__":
    asyncio.run(export_guia_premium())
