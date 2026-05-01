# Padrões de Design - Daiane Borcath Fotografia

## 1. IDENTIDADE VISUAL

### Paleta de Cores
| Nome | Hex | Uso |
|------|-----|-----|
| Dourado Champanhe | `#D4AF37` | Acentos, linhas decorativas, destaques |
| Branco Puro | `#FFFFFF` | Texto principal, overlays claros |
| Preto | `#000000` | Fundo de overlays escuros |
| Bege Quente | `#F8F4E6` | Background alternativo (CTA) |
| Cinza Suave | `#FAFAFA` | Background secundário |
| Texto Secundário | `#666666` | Informações complementares |

### Tipografia
| Elemento | Fonte | Peso | Tamanho (Carrossel) | Tamanho (Stories) |
|----------|-------|------|---------------------|-------------------|
| Títulos | Playfair Display | 600-700 | 44-48px | 52-56px |
| Subtítulos | Playfair Display | 500 | 38-40px | 48px |
| Corpo/Benefícios | Playfair Display Italic | 400 | 36px | 44px |
| Prova Social | Playfair Display | 400 | 34px | 42px |
| CTA Principal | Playfair Display | 700 | 44px | 52px |
| CTA Secundário | Inter | 300 | 17-18px | 20px |
| Numeração | Inter | 300 | 13px | 14px |
| Marca d'água | Inter | 400 | 10-11px | 12px |
| Badge | Inter | 500 | 14px | 16px |

### Espaçamento
- **Padding horizontal:** 72px (carrossel), 80px (stories)
- **Padding bottom texto:** 130px (carrossel), 280px (stories)
- **Gold line margin-bottom:** 28-36px
- **Gap entre elementos:** 18-24px

## 2. DIMENSÕES

| Formato | Largura | Altura | Proporção |
|---------|---------|--------|-----------|
| Carrossel/Feed | 1080px | 1350px | 4:5 |
| Stories | 1080px | 1920px | 9:16 |

## 3. OVERLAYS DE GRADIENTE

### Overlay Padrão
```css
linear-gradient(
    180deg,
    transparent 0%,
    transparent 40%,
    rgba(0,0,0,0.15) 60%,
    rgba(0,0,0,0.50) 78%,
    rgba(0,0,0,0.78) 100%
)
```

### Overlay Strong (textos longos)
```css
linear-gradient(
    180deg,
    rgba(0,0,0,0.20) 0%,
    rgba(0,0,0,0.05) 30%,
    rgba(0,0,0,0.10) 50%,
    rgba(0,0,0,0.55) 75%,
    rgba(0,0,0,0.82) 100%
)
```

### Overlay Warm (CTA)
```css
linear-gradient(
    180deg,
    rgba(30,20,10,0.25) 0%,
    rgba(30,20,10,0.08) 35%,
    rgba(30,20,10,0.12) 55%,
    rgba(25,18,8,0.60) 78%,
    rgba(18,12,5,0.85) 100%
)
```

## 4. ELEMENTOS DECORATIVOS

### Linha Dourada
- Largura: 48px (curta) / 64px (longa)
- Altura: 1px
- Cor: #D4AF37 com opacity 0.6-0.85

### Ponto Dourado
- Tamanho: 10-12px diâmetro
- Cor: #D4AF37
- Uso: marcador de benefícios

### Badge "Agenda Aberta"
- Padding: 10-14px vertical, 28-36px horizontal
- Border: 1px solid #D4AF37
- Fonte: Inter 500, 14-16px
- Cor: #D4AF37
- Letter-spacing: 3-4px
- Text-transform: uppercase

### Sombra de Texto
```css
text-shadow: 0 2px 24px rgba(0,0,0,0.35);
/* Stories: 0 2px 30px rgba(0,0,0,0.4) */
```

## 5. POSICIONAMENTO DE ELEMENTOS

### Numeração de Slide
- Carrossel: top 40px, right 48px
- Stories: top 200px, center

### Marca d'água
- Carrossel: bottom 36px, right 48px
- Stories: bottom 160px, center

### Swipe Hint (Stories)
- Position: bottom 180px, center
- Fonte: Inter 400, 16px
- Cor: rgba(255,255,255,0.4)
- Letter-spacing: 2px

## 6. REGRAS DE COMPOSIÇÃO

1. **Foto em full-bleed** - ocupa 100% do canvas
2. **Texto sempre na zona inferior** (bottom 25-35% carrossel, bottom 30-40% stories)
3. **Alinhamento variado** para criar ritmo visual:
   - Slide 1: centro
   - Slide 2: esquerda
   - Slide 3: centro
   - Slide 4: esquerda (com dot)
   - Slide 5: centro (com dot)
   - Slide 6: direita (com dot)
   - Slide 7: centro
   - Slide 8: centro
4. **Zero repetição de fotos** no mesmo carrossel
5. **Mínimo 2 fotos com 3+ pessoas** para variedade

## 7. FORMATO DE EXPORTAÇÃO

- **Formato:** PNG-24
- **Color Space:** sRGB
- **Qualidade:** Máxima (texto nítido)
- **Metadata:** Removida

## 8. SELEÇÃO DE FOTOS ATUAL

| Slide | Foto | Pessoas | Descrição |
|-------|------|---------|-----------|
| 1 | IMG_7579 | 2 | Duas mulheres se abraçando |
| 2 | IMG_7529 | 2 | Duas mulheres na cama sorrindo |
| 3 | IMG_7491 | 2 | Mulher beijando a cabeça do menino |
| 4 | IMG_7586 | 2 | Mãe e filho olhando um para o outro |
| 5 | IMG_7564 | 3 | Mulher com duas crianças |
| 6 | IMG_7534 | 2 | Mãe e filha na cama abraçadas |
| 7 | IMG_7577 | 2 | Duas mulheres se abraçando |
| 8 | IMG_7478 | 3 | Família posando com filho e mãe |

## 9. COPY PADRONIZADO (Português Correto)

### Hook
> "Este Dia das Mães, presenteie com o que realmente dura"

### Problema
> "Flores murcham. Chocolate acaba.<br>Mas o amor de mãe... *isso é eterno.*"

### Solução
> "Um ensaio de Dia das Mães não é só um presente.<br>**É congelar um momento que ela vai guardar para sempre.**"

### Benefício 1
> "É guardar o sorriso que só ela tem quando te vê"

### Benefício 2
> "É criar um legado que ela vai mostrar com orgulho para a família"

### Benefício 3
> "É ter a certeza de que esse amor está preservado para sempre"

### Agenda Aberta
> "Cada ensaio é uma **história única de amor**.<br>Honrada em fazer parte dessas jornadas."

### CTA
> "Link na bio para garantir seu horário"<br>
> Curitiba e região
