# 🍂 Rua do Outono - Campanha de Fotografia

## 📋 Visão Geral

Landing page e sistema de captação de leads para ensaios fotográficos na Rua do Outono, Curitiba. O projeto integra tráfego pago, captura de leads via Google Apps Script e notificações em tempo real no Telegram.

## 🎯 Objetivo

Captar leads qualificados para ensaios fotográficos promocionais (4-6 fotos gratuitas) com foco em conversão via WhatsApp e upsell de pacotes completos.

## ✅ O que foi entregue

### 1. Landing Page (https://eliuhahner.github.io/leadsfotografia/)
- Design minimalista e premium com tipografia Playfair Display + Inter
- Galeria rotativa (Swiper.js) com 15 fotos selecionadas
- Seção da Rua do Outono (3 fotos + Google Maps embutido)
- Formulário de captura: Nome, WhatsApp, E-mail
- Lógica de sorteio: 80% chance de 5 fotos, 20% de 4 ou 6
- Botão de agendamento via WhatsApp com mensagem dinâmica
- **Performance**: Imagens otimizadas de 15MB $\rightarrow$ ~200-500KB cada

### 2. Automação de Leads
- **Google Apps Script** configurado para enviar notificações via Telegram
- **Integração**: Formulário $\rightarrow$ Google Script $\rightarrow$ Bot Telegram (Daiane recebe leads instantaneamente)
- Endpoint: `https://script.google.com/macros/s/AKfycbySLlEvdsroR4DmwS1hYbfYBz-u7HKM88l7Qu4SPdgzh2U9bVwgrzDxJompyXzz1IwC-w/exec`

### 3. Estratégia de Vendas (WhatsApp)
- Documento `estrategia_vendas.md` com scripts completos
- Abordagem de "Consultora de Memórias" (não vendedora)
- Técnicas de micro-comprometimento
- Gestão de escassez (12 vagas: 09 e 16 de maio)
- Respostas para objeções (preço, vergonha, indecisão)

### 4. Carrossel Instagram
- 6 slides em formato 1080x1350px (proporção 4:5)
- Design editorial (estilo revista/galeria)
- Seguindo rigorosamente o **Design System** (`design_system.md`)
- Layout: Foto em moldura + zona de texto limpa
- Tipografia: Georgia Bold (72pt título, 28pt subtítulo)
- Paleta: Dourado #B35A44, Off-White #FCFCFC
- **Slide 4 com empilhamento vertical** de 3 imagens panorâmicas
- Arquivos finais em: `slides_instagram/slide_1.png` a `slide_6.png`

### 5. Documentação de Design
- `design_system.md`: Diretrizes completas de design
- `carrossel_instagram/DESIGN_PATTERNS.md`: Padrões específicos para mídia social
- Cores, tipografia, espaçamentos, regras de composição

## 🛠️ Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3 (Tailwind CSS), JavaScript (Vanilla)
- **Carrossel**: Swiper.js
- **Backend**: Google Apps Script (Serverless)
- **Notificações**: Telegram Bot API
- **Imagens**: Python (PIL/Pillow) para otimização
- **Hospedagem**: GitHub Pages
- **Controle de Versão**: Git/GitHub

## 📂 Estrutura do Repositório

```
leadsfotografia/
├── index.html                          # Landing page principal
├── assets/
│   ├── img/                         # Imagens otimizadas (PNG/JPG)
│   └── slides/                      # Slides do Instagram (PNG)
├── estrategia_vendas.md                # Gui de vendas WhatsApp
├── design_system.md                   # Sistema de design
├── google_apps_script.gs             # Script de notificações Telegram
├── create_slides.py                   # Gerador de slides (Python)
└── README.md                         # Este arquivo
```

## 🎨 Design Patterns (Instagram)

### Dimensões
- **Feed/Carrossel**: 1080x1350px (4:5)
- **Stories**: 1080x1920px (9:16)

### Cores
| Nome | Hex |
|------|-----|
| Dourado (Primária) | `#B35A44` |
| Off-White | `#FCFCFC` |
| Texto Claro | `#FFFFFF` |
| Texto Escuro | `#333333` |

### Tipografia
| Elemento | Fonte | Peso | Tamanho |
|----------|-------|------|----------|
| Títulos | Georgia Bold | 700 | 54-72px |
| Subtítulos | Georgia Italic | 400 | 28-32px |

## 🚀 Status do Projeto

**✅ CONCLUÍDO**

- [x] Landing page no ar e otimizada
- [x] Captura de leads funcionando (testado)
- [x] Notificações Telegram ativas
- [x] Estratégia de vendas documentada
- [x] Slides Instagram gerados (6 unidades)
- [x] Design system aplicado
- [x] Código versionado no GitHub

## 📞 Próximos Passos (Para a Daiane)

1. **Ativar Campanha**: Configurar anúncios no Meta Ads apontando para a Landing Page
2. **Monitoramento**: Acompanhar leads chegando no Telegram
3. **Conversão**: Aplicar scripts do `estrategia_vendas.md` no WhatsApp
4. **Upsell**: No dia do ensaio, oferecer fotos adicionais (R$ 25,00 cada)

## 📧 Contato

**Daiane Borcath Fotografia**
- Local: Curitiba, PR
- Instagram: @daiane.borcath
- WhatsApp: (41) 99960-5872

---

*Projeto desenvolvido em abril de 2026*
