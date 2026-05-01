"""
Script de exportação do carrossel "10 Objeções" — 10/04/2026
Exporta 12 slides de AMBAS as versões (com foto e só texto).

Uso:
    python export_objecoes.py              # exporta as duas versões
    python export_objecoes.py --foto       # só versão com foto
    python export_objecoes.py --texto      # só versão só-texto
"""
import asyncio
import argparse
import os
from playwright.async_api import async_playwright

SLIDES = [
    ("slide-01", "01_capa"),
    ("slide-02", "02_comportamento"),
    ("slide-03", "03_autoestima"),
    ("slide-04", "04_momento"),
    ("slide-05", "05_fotogenia"),
    ("slide-06", "06_tempo"),
    ("slide-07", "07_financeiro"),
    ("slide-08", "08_valor"),
    ("slide-09", "09_personalidade"),
    ("slide-10", "10_vestir"),
    ("slide-11", "11_procrastinacao"),
    ("slide-12", "12_encerramento"),
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VERSIONS = {
    "foto":  ("objecoes_com_foto.html",  "carrossel_output/objecoes_foto"),
    "texto": ("objecoes_so_texto.html",  "carrossel_output/objecoes_texto"),
}


async def export_version(playwright, html_file: str, output_dir: str):
    out_path = os.path.join(BASE_DIR, output_dir)
    os.makedirs(out_path, exist_ok=True)

    html_abs = os.path.join(BASE_DIR, html_file)
    file_url = f"file:///{html_abs.replace(os.sep, '/')}"

    browser = await playwright.chromium.launch(headless=True)

    for slide_id, slide_name in SLIDES:
        png_path = os.path.join(out_path, f"{slide_name}.png")
        print(f"  Exportando {slide_name}...", end=" ")

        page = await browser.new_page(viewport={"width": 1080, "height": 1350})
        await page.goto(file_url, wait_until="networkidle")
        await page.wait_for_timeout(2500)   # aguarda fontes + imagens

        element = await page.query_selector(f"#{slide_id}")
        if element:
            await element.scroll_into_view_if_needed()
            await page.wait_for_timeout(400)
            await element.screenshot(path=png_path, type="png")
            print(f"✓  → {output_dir}/{slide_name}.png")
        else:
            print(f"✗  ERRO: #{slide_id} não encontrado")

        await page.close()

    await browser.close()


async def main(run_foto: bool, run_texto: bool):
    async with async_playwright() as p:
        if run_foto:
            print("\n▶ Versão COM FOTO")
            await export_version(p, *VERSIONS["foto"])

        if run_texto:
            print("\n▶ Versão SÓ TEXTO")
            await export_version(p, *VERSIONS["texto"])

    print("\n✅ Exportação concluída!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--foto",  action="store_true", help="Exporta só versão com foto")
    parser.add_argument("--texto", action="store_true", help="Exporta só versão só-texto")
    args = parser.parse_args()

    # Se nenhum flag, exporta as duas
    run_foto  = args.foto  or (not args.foto and not args.texto)
    run_texto = args.texto or (not args.foto and not args.texto)

    asyncio.run(main(run_foto, run_texto))
