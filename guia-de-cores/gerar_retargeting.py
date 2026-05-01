#!/usr/bin/env python3
"""
Retargeting Ad Generator - Daiane Borcath
Goal: High Urgency / Conversion for Warm Leads
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# --- CONFIGURAÇÕES DE DESIGN ---
WIDTH, HEIGHT = 1080, 1350
COLORS = {
    "GOLD": (212, 175, 55),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
}

FOTOS_DIR = Path("C:/Users/eliuh/Desktop/Orçamentos Fotografia Daiane/fotos_para_avaliar")
OUTPUT_DIR = Path("C:/Users/eliuh/Desktop/Orçamentos Fotografia Daiane/carrossel_instagram/premium_pb")

def get_font(name, size, bold=False):
    try:
        if "Playfair" in name:
            paths = [
                f"C:/Windows/Fonts/playfairdisplay-bold.ttf" if bold else f"C:/Windows/Fonts/playfairdisplay-regular.ttf",
                "C:/Windows/Fonts/georgia.ttf",
                "times.ttf"
            ]
        else:
            paths = [
                "C:/Windows/Fonts/inter-bold.ttf" if bold else "C:/Windows/Fonts/inter-regular.ttf",
                "C:/Windows/Fonts/arial.ttf",
                "calibri.ttf"
            ]
        for p in paths:
            try: return ImageFont.truetype(p, size)
            except: continue
    except: pass
    return ImageFont.load_default()

def apply_premium_overlay(img):
    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for y in range(HEIGHT):
        if y < HEIGHT * 0.3:
            alpha = 0
        elif y < HEIGHT * 0.75:
            alpha = int(((y - HEIGHT * 0.3) / (HEIGHT * 0.45)) * 180)
        else:
            alpha = int(150 + ((y - HEIGHT * 0.75) / (HEIGHT * 0.25)) * 100)
        draw.line([(0, y), (WIDTH, y)], fill=(0, 0, 0, alpha))
    return Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

def create_retargeting_ad():
    # Foto B&W-2 é a mais emocional (abraço)
    foto_path = FOTOS_DIR / "B&W-2.jpg"
    
    with Image.open(foto_path) as img:
        img = img.convert('RGB')
        # Crop to 4:5
        w, h = img.size
        aspect = WIDTH / HEIGHT
        if w/h > aspect:
            new_w = h * aspect
            left = (w - new_w) / 2
            img = img.crop((left, 0, left + new_w, h))
        else:
            new_h = w / aspect
            top = (h - new_h) / 2
            img = img.crop((0, top, w, top + new_h))
        
        img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
        img = apply_premium_overlay(img)
        draw = ImageDraw.Draw(img)
        
        # 1. Badge de Urgência no Topo
        badge_w, badge_h = 320, 50
        bx = (WIDTH - badge_w) // 2
        draw.rectangle([bx, 60, bx + badge_w, 60 + badge_h], outline=COLORS["GOLD"], width=2)
        badge_font = get_font("Inter", 20, bold=True)
        draw.text((WIDTH // 2, 85), "ÚLTIMAS VAGAS", font=badge_font, fill=COLORS["GOLD"], anchor="mm")
        
        # 2. Título de Impacto
        title_font = get_font("Playfair", 72, bold=True)
        title_text = "Não deixe a memória\nmais linda do ano"
        draw.text((WIDTH // 2, HEIGHT // 2 - 100), title_text, font=title_font, fill=COLORS["WHITE"], anchor="mm", align="center")
        
        # 3. Subtítulo de Fechamento
        sub_font = get_font("Playfair", 42)
        sub_text = "passar em branco."
        draw.text((WIDTH // 2, HEIGHT // 2 + 20), sub_text, font=sub_font, fill=COLORS["GOLD"], anchor="mm")
        
        # 4. Oferta Final na Base
        line_w = 100
        draw.line([(WIDTH // 2 - line_w // 2, HEIGHT - 300), (WIDTH // 2 + line_w // 2, HEIGHT - 300)], fill=COLORS["GOLD"], width=3)
        
        price_font = get_font("Playfair", 60, bold=True)
        draw.text((WIDTH // 2, HEIGHT - 240), "R$ 349", font=price_font, fill=COLORS["WHITE"], anchor="mm")
        
        detail_font = get_font("Inter", 32)
        draw.text((WIDTH // 2, HEIGHT - 180), "ou 12x de R$ 34,90 no cartão", font=detail_font, fill=COLORS["WHITE"], anchor="mm")
        
        # Marca d'água
        logo_font = get_font("Inter", 14)
        draw.text((WIDTH - 72, HEIGHT - 72), "Daiane Borcath", font=logo_font, fill=COLORS["WHITE"])
        
        img.save(OUTPUT_DIR / "retargeting_final_call.png", "PNG")
        print("Criativo de Retargeting gerado com sucesso!")

if __name__ == "__main__":
    create_retargeting_ad()
