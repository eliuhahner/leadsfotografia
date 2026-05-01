#!/usr/bin/env python3
"""
Premium Ad Generator - Daiane Borcath
Design System: Modern Organic Minimalism
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# --- CONFIGURAÇÕES DE DESIGN (DESIGN_PATTERNS.md) ---
WIDTH, HEIGHT = 1080, 1350
COLORS = {
    "GOLD": (212, 175, 55),      # #D4AF37
    "WHITE": (255, 255, 255),    # #FFFFFF
    "BLACK": (0, 0, 0),          # #000000
    "TEXT_SEC": (102, 102, 102)  # #666666
}

# Tipografia (Paths estimados - fallback para serif/sans)
FONTS = {
    "TITLE": "Playfair Display",
    "BODY": "Inter",
}

# Configurações de Espaçamento
PADDING = 72
BOTTOM_TEXT_ZONE = 400

# Mapeamento de Fotos e Textos
SLIDES = [
    {
        "foto": "B&W-2.jpg", 
        "titulo": "O presente que ela\nnunca pediu, mas que",
        "sub": "guardará para sempre",
        "align": "center",
        "type": "hook"
    },
    {
        "foto": "B&W-5.jpg", 
        "titulo": "Flores murcham.\nChocolates acabam.",
        "sub": "Mas as memórias...\nessas são eternas.",
        "align": "left",
        "type": "problem"
    },
    {
        "foto": "B&W.jpg", 
        "titulo": "Uma experiência\nde conexão",
        "sub": "1h de sessão | 15 fotos premium",
        "align": "center",
        "type": "solution"
    },
    {
        "foto": "B&W-10.jpg", 
        "titulo": "R$ 349",
        "sub": "ou 12x de R$ 34,90 no cartão\n📍 Curitiba e Região | Vagas Limitadas",
        "align": "center",
        "type": "price"
    }
]

FOTOS_DIR = Path("C:/Users/eliuh/Desktop/Orçamentos Fotografia Daiane/fotos_para_avaliar")
OUTPUT_DIR = Path("C:/Users/eliuh/Desktop/Orçamentos Fotografia Daiane/carrossel_instagram/premium_pb")

def get_font(name, size, bold=False):
    """Tenta carregar fontes do sistema ou fallbacks de alta qualidade."""
    try:
        if "Playfair" in name:
            # Tentativa de caminhos comuns no Windows
            paths = [
                f"C:/Windows/Fonts/playfairdisplay-bold.ttf" if bold else f"C:/Windows/Fonts/playfairdisplay-regular.ttf",
                "C:/Windows/Fonts/georgia.ttf", # Serif fallback
                "times.ttf"
            ]
        else:
            paths = [
                "C:/Windows/Fonts/inter-bold.ttf" if bold else "C:/Windows/Fonts/inter-regular.ttf",
                "C:/Windows/Fonts/arial.ttf", # Sans fallback
                "calibri.ttf"
            ]
        
        for p in paths:
            try: return ImageFont.truetype(p, size)
            except: continue
    except: pass
    return ImageFont.load_default()

def apply_premium_overlay(img):
    """Aplica o gradiente 'Strong' do design pattern."""
    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Gradiente linear simulado (Strong Overlay)
    for y in range(HEIGHT):
        # 0% a 30% (transparente), 30% a 75% (cresce), 75% a 100% (escuro)
        if y < HEIGHT * 0.3:
            alpha = 0
        elif y < HEIGHT * 0.75:
            alpha = int(((y - HEIGHT * 0.3) / (HEIGHT * 0.45)) * 150)
        else:
            alpha = int(150 + ((y - HEIGHT * 0.75) / (HEIGHT * 0.25)) * 100)
        
        draw.line([(0, y), (WIDTH, y)], fill=(0, 0, 0, alpha))
    
    return Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

def create_premium_slide(slide_data, index):
    # 1. Carregar e preparar Foto
    foto_path = FOTOS_DIR / slide_data["foto"]
    with Image.open(foto_path) as img:
        img = img.convert('RGB')
        # Crop centralizado e resize
        w, h = img.size
        aspect = WIDTH / HEIGHT
        if w/h > aspect:
            # Corta laterais
            new_w = h * aspect
            left = (w - new_w) / 2
            img = img.crop((left, 0, left + new_w, h))
        else:
            # Corta topo/baixo
            new_h = w / aspect
            top = (h - new_h) / 2
            img = img.crop((0, top, w, top + new_h))
        
        img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
        
        # 2. Overlay Premium
        img = apply_premium_overlay(img)
        draw = ImageDraw.Draw(img)
        
        # 3. Elementos de Design
        # Linha Dourada Decorativa
        line_w = 64 if slide_data["align"] == "center" else 48
        lx = WIDTH // 2 - line_w // 2 if slide_data["align"] == "center" else PADDING
        draw.line([(lx, HEIGHT - 600), (lx + line_w, HEIGHT - 600)], fill=COLORS["GOLD"], width=2)

        # 4. Tipografia
        # Título
        title_font = get_font("Playfair", 64, bold=True)
        t_color = COLORS["WHITE"]
        if slide_data["type"] == "price": t_color = COLORS["GOLD"]
        
        # Alinhamento do texto
        text_x = WIDTH // 2 if slide_data["align"] == "center" else PADDING
        text_anchor = "mm" if slide_data["align"] == "center" else "lm"
        
        # Sombra suave para legibilidade
        draw.text((text_x + 2, HEIGHT - 650 + 2), slide_data["titulo"], font=title_font, fill=(0,0,0,100), anchor=text_anchor)
        draw.text((text_x, HEIGHT - 650), slide_data["titulo"], font=title_font, fill=t_color, anchor=text_anchor)

        # Subtítulo / Corpo
        if slide_data["sub"]:
            sub_font = get_font("Playfair", 36) # Italic feel
            draw.text((text_x, HEIGHT - 560), slide_data["sub"], font=sub_font, fill=COLORS["WHITE"], anchor=text_anchor)

        # Badge Topo
        badge_w, badge_h = 240, 40
        bx = (WIDTH - badge_w) // 2
        draw.rectangle([bx, 60, bx + badge_w, 60 + badge_h], outline=COLORS["GOLD"], width=1)
        badge_font = get_font("Inter", 16, bold=True)
        draw.text((WIDTH // 2, 80), "DIA DAS MÃES", font=badge_font, fill=COLORS["GOLD"], anchor="mm")

        # Numeração e Marca
        num_font = get_font("Inter", 14)
        draw.text((WIDTH - PADDING, 40), f"{index + 1}/4", font=num_font, fill=COLORS["WHITE"])
        draw.text((WIDTH - PADDING, HEIGHT - PADDING), "Daiane Borcath", font=num_font, fill=COLORS["WHITE"])

    return img

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for i, data in enumerate(SLIDES):
        print(f"Gerando slide {i+1}...")
        slide = create_premium_slide(data, i)
        slide.save(OUTPUT_DIR / f"slide_{i+1:02d}_premium_pb.png", "PNG")

if __name__ == "__main__":
    main()
