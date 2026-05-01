# CONTEXTO COMPLETO DO PROJETO — Daiane Borcath Fotografia
## Campanha Dia das Mães 2026

> **Instrução para IA:** Este documento contém TODO o contexto necessário para continuar este projeto do zero. Leia tudo antes de qualquer ação.

---

## 1. DADOS DO NEGÓCIO

| Campo | Valor |
|-------|-------|
| **Nome** | Daiane Borcath Fotografia |
| **Serviço** | Ensaios fotográficos profissionais |
| **Especialidade** | Ensaios maternos, familiares, Dia das Mães |
| **Localização** | Curitiba e região metropolitana |
| **Experiência** | 6 meses |
| **Público-alvo** | Mães de alta renda, 25-45 anos, classe A/B |
| **Arquétipo de marca** | Inspiracional + Emocional |
| **Tom de voz** | Sofisticado e acolhedor (luxo acessível) |

---

## 2. PADRÕES DE DESIGN

### Paleta de Cores
| Nome | Hex | Uso |
|------|-----|-----|
| Dourado Champanhe | `#D4AF37` | Acentos, linhas, destaques, badges |
| Branco Puro | `#FFFFFF` | Texto principal |
| Preto | `#000000` | Fundo de overlays escuros |
| Bege Quente | `#F8F4E6` | Background alternativo (CTA) |
| Cinza Suave | `#FAFAFA` | Background secundário |
| Texto Secundário | `#666666` | Informações complementares |

### Tipografia
| Elemento | Fonte | Peso | Feed | Stories |
|----------|-------|------|------|---------|
| Títulos | Playfair Display | 600-700 | 44-52px | 52-56px |
| Subtítulos | Playfair Display | 500 | 38-40px | 48px |
| Corpo/Benefícios | Playfair Display Italic | 400 | 36px | 44px |
| CTA Principal | Playfair Display | 700 | 44px | 52px |
| CTA Secundário | Inter | 300 | 17-18px | 20px |
| Numeração | Inter | 300 | 13px | 14px |
| Marca d'água | Inter | 400 | 10-11px | 12px |
| Badge | Inter | 500 | 14-15px | 16px |

### Dimensões
| Formato | Largura | Altura | Proporção |
|---------|---------|--------|-----------|
| Carrossel/Feed | 1080px | 1350px | 4:5 |
| Stories | 1080px | 1920px | 9:16 |

### Overlays de Gradiente (para texto sobre fotos full-bleed)
```css
/* Overlay Padrão */
linear-gradient(180deg, transparent 0%, transparent 40%, rgba(0,0,0,0.15) 60%, rgba(0,0,0,0.50) 78%, rgba(0,0,0,0.78) 100%)

/* Overlay Strong (textos longos) */
linear-gradient(180deg, rgba(0,0,0,0.20) 0%, rgba(0,0,0,0.05) 30%, rgba(0,0,0,0.10) 50%, rgba(0,0,0,0.55) 75%, rgba(0,0,0,0.82) 100%)

/* Overlay Warm (CTA) */
linear-gradient(180deg, rgba(30,20,10,0.25) 0%, rgba(30,20,10,0.08) 35%, rgba(30,20,10,0.12) 55%, rgba(25,18,8,0.60) 78%, rgba(18,12,5,0.85) 100%)
```

### Elementos Decorativos
- **Linha dourada:** 48px × 1px (#D4AF37, opacity 0.6-0.85)
- **Ponto dourado:** 10-12px diâmetro, #D4AF37, border-radius 50%
- **Badge:** Border 1px solid #D4AF37, padding 10-14px vertical + 28-36px horizontal, Inter 500 14-16px, letter-spacing 3-4px, uppercase
- **Sombra de texto:** `text-shadow: 0 2px 24px rgba(0,0,0,0.35)` (feed) / `0 2px 30px rgba(0,0,0,0.4)` (stories)

### Regras de Composição
1. Foto em **full-bleed** (100% do canvas)
2. Texto sempre na **zona inferior** (bottom 25-35% feed, bottom 30-40% stories)
3. Alinhamento variado para ritmo visual (centro, esquerda, direita)
4. **Zero repetição de fotos** no mesmo carrossel
5. Mínimo **2 fotos com 3+ pessoas** para variedade
6. Marca d'água discreta bottom-right (feed) ou bottom-center (stories)

### Exportação
- **Formato:** PNG-24
- **Color Space:** sRGB
- **Ferramenta:** Playwright (Chromium headless) + Python
- **Scripts:** `export_slides.py`, `export_stories.py`, `export_posts.py`, `export_coringa.py`

---

## 3. SELEÇÃO DE FOTOS (8 fotos, zero repetições)

| Slide | Foto | Pessoas | Descrição | Score |
|-------|------|---------|-----------|-------|
| 1 | IMG_7579 | 2 | Duas mulheres se abraçando | 28,87 |
| 2 | IMG_7529 | 2 | Duas mulheres na cama sorrindo | 28,46 |
| 3 | IMG_7491 | 2 | Mulher beijando a cabeça do menino | 25,38 |
| 4 | IMG_7586 | 2 | Mãe e filho olhando um para o outro | 25,10 |
| 5 | IMG_7564 | 3 | Mulher com duas crianças | 26,56 |
| 6 | IMG_7534 | 2 | Mãe e filha na cama abraçadas | 26,29 |
| 7 | IMG_7577 | 2 | Duas mulheres se abraçando | 26,11 |
| 8 | IMG_7478 | 3 | Família posando com filho e mãe | 27,17 |

**Fotos recusadas pelo usuário:** IMG_7490, IMG_7495, IMG_7576, IMG_7573, IMG_7479
**Motivo:** Posing rígido, genérico, ou não representavam conexão genuína

---

## 4. COPY PADRONIZADO (Português Correto)

### Hook
> "Este Dia das Mães, presenteie com o que realmente dura"

### Problema
> "Flores murcham. Chocolate acaba. Mas o amor de mãe... *isso é eterno.*"

### Solução
> "Um ensaio de Dia das Mães não é só um presente. **É congelar um momento que ela vai guardar para sempre.**"

### Benefício 1
> "É guardar o sorriso que só ela tem quando te vê"

### Benefício 2
> "É criar um legado que ela vai mostrar com orgulho para a família"

### Benefício 3
> "É ter a certeza de que esse amor está preservado para sempre"

### Agenda Aberta
> "Cada ensaio é uma **história única de amor**. Honrada em fazer parte dessas jornadas."

### CTA
> "Link na bio para garantir seu horário" / "Curitiba e região"

---

## 5. CALENDÁRIO DE POSTAGENS (06/04 a 08/05/2026)

**Frequência:** 3x/semana (segunda, quarta, sexta)
**Horários:** Feed 11h30 ou 18h30 | Stories 8h30, 11h, 14h, 18h, 20h

### SEMANA 1 — CONSCIÊNCIA (06-10/04)
| Data | Hora | Formato | Tema | Arquivo | Status |
|------|------|---------|------|---------|--------|
| 06/04 seg | 11h30 | Carrossel 8 slides | "Memórias que Não Voltam" | 01_hook a 08_cta.png | ✅ Pronto |
| 08/04 qua | 18h30 | Foto única | Bastidores — "O que acontece antes do clique" | post_bastidores.png | ✅ Pronto |
| 10/04 sex | 12h00 | Reels 30-45s | "3 motivos para presentear com ensaio" | 📝 Roteiro pronto ✅ |

### SEMANA 2 — CONEXÃO (13-17/04)
| Data | Hora | Formato | Tema | Arquivo | Status |
|------|------|---------|------|---------|--------|
| 13/04 seg | 11h30 | Carrossel 6-8 slides | "O que as mães realmente querem ganhar" | 📝 Roteiro |
| 15/04 qua | 18h30 | Foto única + Depoimento | "O que uma cliente disse depois do ensaio" | post_depoimento.png | ✅ Pronto |
| 17/04 sex | 12h00 | Reels 30-45s | "Como é um ensaio de Dia das Mães comigo" | 📝 Roteiro pronto ✅ |

### SEMANA 3 — CONSIDERAÇÃO (20-24/04)
| Data | Hora | Formato | Tema | Arquivo | Status |
|------|------|---------|------|---------|--------|
| 20/04 seg | 11h30 | Carrossel 6-8 slides | "Ensaio vs presentes tradicionais" | 📝 Roteiro |
| 22/04 qua | 18h30 | Foto única | "A foto que toda mãe guarda na cabeceira" | post_foto_cabeceira.png | ✅ Pronto |
| 24/04 sex | 12h00 | Reels 30-45s | "Antes e depois — a transformação" | 📝 Roteiro pronto ✅ |

### SEMANA 4 — CONVERSÃO (27/04-01/05)
| Data | Hora | Formato | Tema | Arquivo | Status |
|------|------|---------|------|---------|--------|
| 27/04 seg | 11h30 | Carrossel 6-8 slides | "O que está incluso no ensaio" | 📝 Roteiro |
| 29/04 qua | 18h30 | Foto única | "Faltam 11 dias — agenda quase lotada" | post_urgencia.png | ✅ Pronto |
| 01/05 sex | 12h00 | Reels 30-45s | "Perguntas frequentes (FAQ)" | 📝 Roteiro |

### SEMANA 5 — URGÊNCIA FINAL (04-08/05)
| Data | Hora | Formato | Tema | Arquivo | Status |
|------|------|---------|------|---------|--------|
| 04/05 seg | 11h30 | Carrossel 5-6 slides | "Falta 1 semana — ainda dá tempo" | 📝 Roteiro |
| 06/05 qua | 18h30 | Foto única | "Faltam 4 dias — não deixe sem presente" | post_4dias.png | ✅ Pronto |
| 08/05 sex | 12h00 | Reels 15-30s | "Última chamada — ensaios até sábado" | 📝 Roteiro pronto ✅ |

> 📝 Roteiros dos Reels: `skills/instagram-reels-fotografia-materna/roteiros/roteiros_dia_das_maes.md` |

---

## 6. POST CORINGA — TRÁFEGO PAGO

**Veiculação:** 06/04 a 08/05/2026 (33 dias contínuos)
**Orçamento:** R$ 15-30/dia (R$ 495-990 total)
**Formato:** Carrossel 4 slides (1080x1350px)

| Slide | Arquivo | Conteúdo |
|-------|---------|----------|
| 1 | coringa_01_hook.png | "O presente que toda mãe quer — e nunca pede" |
| 2 | coringa_02_problema.png | "Flores murcham. Chocolate acaba..." |
| 3 | coringa_03_beneficios.png | Lista de benefícios do pacote |
| 4 | coringa_04_cta.png | "Agenda aberta — Toque para agendar" |

### Públicos do Gerenciador de Anúncios
1. **Principal:** Curitiba +30km, 25-45 anos, interesses (Dia das Mães, Fotografia, Maternidade, Famílias, Presentes), classe A/B
2. **Lookalike:** 1-3% baseado em clientes anteriores ou seguidores engajados
3. **Remarketing:** Quem interagiu com Instagram nos últimos 30 dias

### Otimização Semanal
| Semana | Ação |
|--------|------|
| 1 | Aprendizado — não mexer nos primeiros 4 dias |
| 2 | Ajuste fino — trocar hook se CTR < 1%, aumentar se > 2,5% |
| 3 | Escala — aumentar orçamento se CPA bom |
| 4 | Urgência — atualizar texto, aumentar orçamento |
| 5 | Última chamada — orçamento máximo, encerrar 08/05 20h |

---

## 7. ESTRUTURA DE ARQUIVOS

```
Orçamentos Fotografia Daiane/
├── carrossel_instagram/
│   ├── 01_hook.png a 08_cta.png          # Carrossel feed (8 slides)
│   ├── story_01_hook.png a story_08_cta.png # Stories (8 partes)
│   ├── post_bastidores.png               # Post 08/04
│   ├── post_depoimento.png               # Post 15/04
│   ├── post_foto_cabeceira.png           # Post 22/04
│   ├── post_urgencia.png                 # Post 29/04
│   ├── post_4dias.png                    # Post 06/05
│   ├── coringa_01_hook.png a coringa_04_cta.png # Post pago (4 slides)
│   ├── carousel.html                     # Template HTML carrossel
│   ├── stories.html                      # Template HTML stories
│   ├── post_coringa.html                 # Template HTML coringa
│   ├── post_foto_cabeceira.html          # Template HTML post único
│   ├── post_urgencia.html                # Template HTML urgência
│   ├── post_4dias.html                   # Template HTML 4 dias
│   ├── post_bastidores.html              # Template HTML bastidores
│   ├── post_depoimento.html              # Template HTML depoimento
│   ├── export_slides.py                  # Script export carrossel
│   ├── export_stories.py                 # Script export stories
│   ├── export_posts.py                   # Script export posts únicos
│   ├── export_coringa.py                 # Script export coringa
│   └── DESIGN_PATTERNS.md                # Documentação de design
│
├── calendario_dia_das_maes/
│   ├── CALENDARIO_MESTRE.md              # Calendário completo atualizado
│   ├── post_coringa_trafego_pago/
│   │   └── GUIA_TRAFEGO_PAGO.md          # Guia completo de tráfego pago
│   ├── 2026-04-06_segunda/POST_01.md
│   ├── 2026-04-08_quarta/POST_02.md
│   ├── 2026-04-10_sexta/POST_03.md
│   ├── 2026-04-13_segunda/POST_04.md
│   ├── 2026-04-15_quarta/POST_05.md
│   ├── 2026-04-17_sexta/POST_06.md
│   ├── 2026-04-20_segunda/POST_07.md
│   ├── 2026-04-22_quarta/POST_08.md
│   ├── 2026-04-24_sexta/POST_09.md
│   ├── 2026-04-27_segunda/POST_10.md
│   ├── 2026-04-29_quarta/POST_11.md
│   ├── 2026-05-01_sexta/POST_12.md
│   ├── 2026-05-04_segunda/POST_13.md
│   ├── 2026-05-06_quarta/POST_14.md
│   └── 2026-05-08_sexta/POST_15.md
│
├── fotos_para_avaliar/                   # Fotos originais (145 arquivos)
└── relatorio_avaliacao.html              # Relatório de avaliação das fotos
```

---

## 8. LIÇÕES APRENDIDAS (NÃO REPETIR ERROS)

### ❌ Erros cometidos:
1. **Texto sem acentos no HTML** — codificação de caracteres corrompeu (ç, ã, é, etc.)
   - **Solução:** Usar `charset="UTF-8"` e escrever texto diretamente com acentos
2. **Fotos com posing rígido** — IMG_7490, IMG_7495, IMG_7576 foram recusadas
   - **Solução:** Priorizar fotos com conexão genuína, não posadas
3. **Fotos repetidas** — IMG_7586 foi usada em 2 slides
   - **Solução:** Verificar unicidade antes de finalizar
4. **Design com muito espaço em branco** — fotos pequenas, cortadas
   - **Solução:** Full-bleed com overlays, texto na zona inferior
5. **Prova social inflada** — "200+ mães" não condizia com 6 meses de experiência
   - **Solução:** Usar abordagem autêntica ("história única de amor")

### ✅ O que funcionou:
1. **Full-bleed photos** — fotos ocupam 100% do canvas
2. **Gradientes overlay** — texto legível sobre fotos
3. **Alinhamento variado** — centro/esquerda/direita cria ritmo visual
4. **Badge "Agenda Aberta"** — elemento de urgência elegante
5. **Copy emocional** — foco em memórias, legado, amor eterno

---

## 9. COMANDOS DE EXPORTAÇÃO

```bash
# Carrossel (8 slides)
python export_slides.py

# Stories (8 partes)
python export_stories.py

# Posts únicos (5 fotos)
python export_posts.py

# Post coringa (4 slides)
python export_coringa.py
```

Todos os scripts usam **Playwright + Chromium headless** e exportam PNG em 1080x1350px (feed) ou 1080x1920px (stories).

---

## 10. HASHTAGS POR FASE

### Consciência (Semana 1):
`#diadasmaes #presentediamães #ensaiofotografico #fotografiadamae #memóriasdefamilia #mãefotografada #curitibafotografia #fotógrafacuritiba #legadofotografico #ensaioesmaterno`

### Conexão (Semana 2):
`#maternidade #amordefilho #momlife #mamae #maternidadeautentica #registrosdefamilia #ensaiofamiliar #fotografiadefamilia #momentosmaternos #fotógrafademarketing`

### Consideração (Semana 3):
`#presentequefica #presenteinesquecivel #ensaiofotografico #fotografiaprofissional #ensaioespecial #diadasmaes2026 #curitiba #regiaocuritiba #fotografiamaterna #presenteparamae`

### Conversão (Semana 4):
`#agendaaberta #ensaiodamae #diadasmaes #ultimasvagas #fotografiadamae #presentediamães #ensaioespecial #curitibafotografia #agendeseuensaio #fotógrafacuritiba`

### Urgência (Semana 5):
`#ultimachamada #diadasmaes #naodeixepraultimahora #presenteurgente #ensaiodamae #agendeseuensaio #curitiba #fotógrafacuritiba #diadasmaes2026 #presenteparamae`

---

## 11. ITENS PENDENTES

| Item | Prioridade | Detalhes |
|------|------------|----------|
| ~~Definir preço do pacote~~ | ~~Alta~~ | ~~R$ 349 ou 12x R$ 35~~ ✅ |
| Produzir Reels (4 vídeos) | Alta | 4 roteiros prontos em `skills/instagram-reels-fotografia-materna/roteiros/` |
| Criar carrosséis das semanas 2,3,4,5 | Média | Precisa de HTML + exportação |
| ~~Configurar link da bio~~ | ~~Alta~~ | ~~wa.me/5541999605872~~ ✅ |
| Configurar campanha de anúncios | Alta | Gerenciador do Meta |
| ~~Preparar respostas padrão~~ | ~~Média~~ | ~~Já documentadas no GUIA_TRAFEGO_PAGO.md~~ ✅ |

---

## 12. SKILLS UTILIZADAS

- **instagram-reels-fotografia-materna** — Roteiros para Reels, templates, prompts geradores
- **short-video-maker** — Ferramenta para criar vídeos curtos (texto + música)
- **sales-instagram-materno** — Templates de carrossel, estratégias de funil, hashtags
- **expert-graphic-designer** — Design minimalista premium para alta renda
- **expert-web-developer** — Implementação HTML/CSS + exportação via Playwright

---

**Última atualização:** 07/04/2026
**Dia das Mães 2026:** 10/05/2026 (domingo)
**Dias restantes:** 33 dias
