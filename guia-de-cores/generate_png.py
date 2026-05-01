import os
from playwright.sync_api import sync_playwright

print("Iniciando geracao de PNGs...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1080, "height": 1350})
    
    path = os.path.abspath("carousel_dia_das_maes.html")
    url = f"file:///{path}"
    
    print(f"Carregando {url}...")
    page.goto(url, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(2000)
    
    slides = [
        ("slide-1", "01_hook"),
        ("slide-2", "02_problema"),
        ("slide-3", "03_solucao"),
        ("slide-4", "04_beneficio1"),
        ("slide-5", "05_beneficio2"),
        ("slide-6", "06_beneficio3"),
        ("slide-7", "07_agenda"),
        ("slide-8", "08_cta"),
    ]
    
    output_dir = "carrossel_output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for slide_id, filename in slides:
        print(f"Capturando {filename}...")
        try:
            page.evaluate(f'''
                document.getElementById('{slide_id}').scrollIntoView();
            ''')
            page.wait_for_timeout(500)
            
            element = page.locator(f"#{slide_id}")
            element.screenshot(path=f"{output_dir}/{filename}.png")
            print(f"  OK Salvo: {output_dir}/{filename}.png")
        except Exception as e:
            print(f"  ERRO em {filename}: {e}")
    
    browser.close()
    print(f"Pronto! PNGs gerados na pasta: {output_dir}")
