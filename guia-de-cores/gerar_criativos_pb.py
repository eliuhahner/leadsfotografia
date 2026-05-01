#!/usr/bin/env python3
"""
Gerador de Criativos P&B para Meta Ads
Usa o padrão de design da Daiane Borcath
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configurações
INPUT_DIR = Path("C:/Users/eliuh/Desktop/Orçamentos Fotografia Daiane/carrossel_instagram")
OUTPUT_DIR = Path("C:/Users/eliuh/Desktop/Orçamentos Fotografia Daiane/carrossel_instagram/criativos_pb")
FOTOS_DIR = Path("C:/Users/eliuh/Desktop/Orçamentos Fotografia Daiane/fotos_para_avaliar")

# Dimensões
WIDTH, HEIGHT = 1080, 1350

# Cores (do DESIGN_PATTERNS)
DOURADO = "#D4AF37"
BRANCO = "#FFFFFF"
PRETO = "#000000"
BEGE = "#F8F4E6"

# Preço
PRECO = "R$ 349"

# Fotos escolhidas para os slides (do DESIGN_PATTERNS)
FOTOS_SLIDES = [
    ("IMG_7579", "Hook emocional"),
    ("IMG_7586", "Conexão"),
    ("IMG_7564", "Familia"),
    ("IMG_7534", "Abraço"),
]

# Texts por slide
TEXTOS = {
    0: {
        "titulo": "Este Dia das Mães,\npresenteie com o que dura",
        "subtitulo": None,
    },
    1: {
        "titulo": "Flores murcham.\nChocolate acaba.",
        "subtitulo": "Mas o amor de mãe...\né eterno.",
    },
    2: {
        "titulo": "1 hora de sessão",
        "subtitulo": "15 fotos editadas em alta",
    },
    3: {
        "titulo": f"{PRECO}",
        "subtitulo": "50% de sinal via PIX\nCuritiba e região",
    },
}


def aplicar_preto_branco(img: Image.Image) -> Image.Image:
    """Converte para P&B com contraste moderado."""
    # Converter para escala de cinza
    gray = img.convert("L")
    
    # Aumentar contraste
    enhancer = ImageEnhance.Contrast(gray)
    gray = enhancer.enhance(1.15)
    
    # Converter de volta para RGB para poder colorir
    img_pb = gray.convert("RGB")
    
    # Aplicar tom sépia suave (aquecimento)
    pixels = img_pb.load()
    for i in range(img_pb.width):
        for j in range(img_pb.height):
            r, g, b = pixels[i, j]
            # Tom levemente aquecido (sépia light)
            new_r = min(255, int(r * 1.05))
            new_g = g
            new_b = min(200, int(b * 0.90))
            pixels[i, j] = (new_r, new_g, new_b)
    
    return img_pb


def criar_overlay_gradiente(draw: ImageDraw.Draw, width: int, height: int):
    """Cria overlay de gradiente para texto."""
    # Simular gradiente com retângulos semitransparentes
    for y in range(height):
        alpha = 0
        if y > height * 0.50:
            alpha = int((y - height * 0.50) / (height * 0.50) * 180)
        elif y > height * 0.40:
            alpha = int((y - height * 0.40) / (height * 0.10) * 50)
        
        if alpha > 0:
            draw.rectangle([(0, y), (width, y + 3)], fill=(0, 0, 0, alpha))


def carregar_fonte(tamanho: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Carrega fonte com fallback."""
    fontes_tentativas = [
        f"C:/Users/eliuh/AppData/Local/Microsoft/Windows/Fonts/PlayfairDisplay-Bold.ttf" if bold 
        else f"C:/Users/eliuh/AppData/Local/Microsoft/Windows/Fonts/PlayfairDisplay-Regular.ttf",
        f"C:/Windows/Fonts/PlayfairDisplay-Bold.ttf" if bold else f"C:/Windows/Fonts/PlayfairDisplay.ttf",
        "arial.ttf",
    ]
    
    for fonte_path in fontes_tentativas:
        try:
            return ImageFont.truetype(fonte_path, tamanho)
        except:
            continue
    
    return ImageFont.load_default()


def criar_slide(nome_foto: str, num_slide: int, texto: dict) -> Image.Image:
    """Cria um slide do carrossel."""
    logger.info(f"Criando slide {num_slide + 1}: {nome_foto}")
    
    # Buscar foto
    foto_path = None
    for ext in ['.jpg', '.jpeg', '.png']:
        potencial = FOTOS_DIR / f"{nome_foto}{ext}"
        if potencial.exists():
            foto_path = potencial
            break
        
        potencial = INPUT_DIR / f"{nome_foto}.jpg"
        if potencial.exists():
            foto_path = potencial
            break
    
    if not foto_path:
        logger.warning(f"Foto não encontrada: {nome_foto}")
        # Criar imagem preta como fallback
        img = Image.new('RGB', (WIDTH, HEIGHT), PRETO)
        return img
    
    # Abrir e processar imagem
    with Image.open(foto_path) as img:
        # Redimensionar para cover (1080x1350)
        img = img.convert('RGB')
        img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
        
        # Aplicar P&B
        img = aplicar_preto_branco(img)
        
        # Criar overlay para texto
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        criar_overlay_gradiente(draw, WIDTH, HEIGHT)
        
        # Combinar
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
        
        # Adicionar texto
        draw = ImageDraw.Draw(img)
        
        # Título
        if texto.get("titulo"):
            fonte_titulo = carregar_fonte(52, bold=True)
            # Sombra do texto
            draw.text((WIDTH//2 + 2, 320 + 2), texto["titulo"], font=fonte_titulo, fill=(0, 0, 0, 180), anchor="mm")
            draw.text((WIDTH//2, 320), texto["titulo"], font=fonte_titulo, fill=BRANCO, anchor="mm")
        
        # Subtítulo
        if texto.get("subtitulo"):
            fonte_sub = carregar_fonte(36, bold=False)
            draw.text((WIDTH//2 + 2, 480 + 2), texto["subtitulo"], font=fonte_sub, fill=(0, 0, 0, 150), anchor="mm")
            draw.text((WIDTH//2, 480), texto["subtitulo"], font=fonte_sub, fill=DOURADO, anchor="mm")
        
        # Linha dourada
        y_linha = 580
        draw.line([(WIDTH//2 - 80, y_linha), (WIDTH//2 + 80, y_linha)], fill=DOURADO, width=2)
        
        # Preço grande no último slide
        if num_slide == 3:
            fonte_preco = carregar_fonte(72, bold=True)
            draw.text((WIDTH//2 + 3, 680 + 3), PRECO, font=fonte_preco, fill=(0, 0, 0, 200), anchor="mm")
            draw.text((WIDTH//2, 680), PRECO, font=fonte_preco, fill=DOURADO, anchor="mm")
        
        # Badge "Dia das Mães" no topo
        badge_y = 60
        draw.rectangle([(WIDTH//2 - 140, badge_y), (WIDTH//2 + 140, badge_y + 45)], outline=DOURADO, width=1)
        fonte_badge = carregar_fonte(16)
        draw.text((WIDTH//2, badge_y + 24), "DIA DAS MÃES", font=fonte_badge, fill=DOURADO, anchor="mm")
        
        # Número do slide
        fonte_num = carregar_fonte(14)
        draw.text((WIDTH - 48, 40), f"{num_slide + 1}/4", font=fonte_num, fill=(255, 255, 255, 150))
        
        # Marca d'água
        draw.text((WIDTH - 48, HEIGHT - 36), "Daidiane Borcath", font=fonte_num, fill=(255, 255, 255, 100))
    
    return img


def main():
    """Gera todos os slides do carrossel."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    logger.info("Iniciando geração de criativos P&B...")
    
    for i, (nome_foto, desc) in enumerate(FOTOS_SLIDES):
        texto = TEXTOS.get(i, {"titulo": "", "subtitulo": ""})
        
        slide = criar_slide(nome_foto, i, texto)
        
        output_path = OUTPUT_DIR / f"slide_{i+1:02d}_pb.png"
        slide.save(output_path, "PNG", quality=95)
        logger.info(f"Salvo: {output_path}")
    
    logger.info("Concluído! Criativos gerados em:")
    logger.info(f"  {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
