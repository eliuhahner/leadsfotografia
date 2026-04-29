# 📋 Dossiê Técnico de Campanha - Rua do Outono 2026

Este documento contém o histórico técnico, decisões de design e configurações de rastreamento da campanha de captação de leads para Daiane Borcath Fotografia.

---

## 🚀 Informações Gerais
- **Cliente:** Daiane Borcath Fotografia
- **Campanha:** Rua do Outono 2026 (Curitiba)
- **Domínio Principal:** [daianeborcathfotografia.com.br](https://daianeborcathfotografia.com.br)
- **Objetivo:** Captação de leads para ensaios gratuitos (5 fotos de presente) com foco em upsell posterior.

---

## 🛠️ Stack Tecnológica
- **Frontend:** HTML5, Tailwind CSS (via CDN), Swiper.js (Galeria).
- **Backend (Serverless):** Google Apps Script (Processamento de formulário e envio para Telegram).
- **Notificações:** Bot de Telegram dedicado para recebimento instantâneo de leads.
- **Hospedagem:** GitHub Pages.

---

## 📊 Rastreamento e Analytics (Setup Sênior)
| Ferramenta | ID / Configuração | Objetivo |
| :--- | :--- | :--- |
| **Meta Pixel** | `931754726341056` | Rastreio de `PageView` e evento customizado de `Lead`. |
| **Microsoft Clarity** | `wjbg65mc69` | Mapas de calor, gravações de sessão e análise de scroll. |
| **Abacus API** | `daianeborcath/outono` | Contador de visitas único e diário para dashboard privado. |
| **Dashboard** | `/metricas.html` | Visualização em tempo real da performance de acessos. |
| **IP Capture** | Integrado (via `ipify`) | Registro do IP do visitante junto aos dados do lead. |

---

## 🎯 Estratégias de CRO (Otimização de Conversão)
1. **Message Match:** Hero Section ajustada para comunicar a oferta nos primeiros 2 segundos.
2. **Fricção Reduzida:** Remoção do campo de e-mail; formulário agora pede apenas Nome e WhatsApp.
3. **Design Card:** Formulário destacado em um card branco com sombra profunda (`shadow-2xl`) para foco total.
4. **Urgência sutil:** Aviso de "Vagas Limitadas" e FAQ Acordeão para quebra de objeções.
5. **Mobile First:** Barra de CTA fixa no rodapé e botão de WhatsApp flutuante.
6. **Performance:** Implementação de `loading="lazy"` em todas as imagens e animações de `reveal` suaves.

---

## 📈 Histórico de Performance Ads (Referência)
- **Início:** 29/04/2026
- **Orçamento:** R$ 40,00/dia
- **Custo por Clique (CPC/LPV):** ~R$ 0,27
- **Público:** [Aguardando validação detalhada]

---
*Última atualização: 29/04/2026 às 14:00*
