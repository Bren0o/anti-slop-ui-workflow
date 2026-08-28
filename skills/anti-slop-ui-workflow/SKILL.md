---
name: anti-slop-ui-workflow
description: Fluxo completo para tirar "AI slop" de interfaces geradas por IA — auditar com Impeccable (detect/init/audit/typeset/adapt/harden/polish), puxar referências visuais (Dribbble, dark.design, LazyWeb MCP), montar com componentes prontos (Shoogle/shadcn) e polir de volta aos tokens do projeto. Use quando o usuário pedir landing page, hero, pricing, dashboard ou qualquer UI hi-fi, quando disser que a tela "parece feita por IA", ou antes de entregar frontend gerado por agente. A skill ui-ux-pro-max só pode servir de rascunho descartável (passo 0), nunca de entrega.
---

# Anti-Slop UI Workflow

Baseado no vídeo "Remova Essa Skill de UI do Seu Projeto AGORA" (youtube.com/watch?v=GdzswgxcqPg).
Transcrição consolidada: `Documents/Dev/Endereços Itaquaquecetuba/transcricao-video-GdzswgxcqPg/TRANSCRICAO-FINAL.md`.

## Princípio

Uma skill é uma instrução **estática**. Se todo mundo usa a mesma base (UI/UX Pro Max, 120k
estrelas), todo mundo gera a mesma tela: gradiente no título, palavra em destaque, três cards,
navbar + texto à esquerda/imagem à direita. Quanto mais detalhado o prompt, mais genérico o
resultado. Por isso:

1. **`ui-ux-pro-max` nunca é o produto final.** No máximo, é o rascunho descartável do passo 0
   (é assim que o vídeo a usa: gera a "landing cobaia" e depois desmonta o slop dela com o
   Impeccable). Nunca entregar o que ela gerou sem passar pelos passos 1–7.
2. **Copiar referência real + polir** vence "gerar do zero".
3. **Não é milagre.** Impeccable melhora acessibilidade, hierarquia, tokens e robustez — não
   transforma vibe-code em site premiado. Gosto vem de olhar referência e de ler as regras.

## Como reconhecer AI slop (2025/2026)

- Mistura excessiva de fontes, serif itálica "estilo Anthropic"
- Fundo com grid de pontos/linhas + gradiente radial
- Gradiente no headline com uma palavra destacada
- Três cards iguais com ícone em cima
- Card "flutuando" à direita do hero
- Estrutura navbar → hero (texto esq. / imagem dir.) → 3 features → pricing → CTA, sempre igual

Catálogo nomeado com o motivo de cada padrão: https://impeccable.style/slop
Detector automático (baseado em padrões — **não é exato**, acha "slop" até no GitHub; use o
olho para confirmar): `npx impeccable detect https://site.com` ou a extensão Chrome.

## Fluxo — na ordem, sem pular

### 0. Rascunho descartável (o "modelo" que vai ser desmontado)
Se ainda não existe tela nenhuma, gere um rascunho rápido com um prompt curto — pode ser com
`ui-ux-pro-max`, como no vídeo (`landing page de ferramenta de CI chamada FlowBase`), ou com
qualquer gerador. Regras do rascunho:
- Prompt **curto**. Quanto mais especificação, mais genérico o resultado dessa skill.
- Aceitar que vai sair slop: gradiente no título, card flutuando à direita, três cards. É o
  ponto de partida para medir e corrigir, não a entrega.
- Se já existe uma tela (legada, vibe-coded, do Gemini/v0/Lovable), pular direto para o passo 1.

Depois, medir a baseline e instalar o Impeccable:
```bash
npx impeccable detect http://localhost:3000   # baseline: quantos padrões de slop
npx impeccable install                        # responder "project" (não global); aceitar hooks
```
Reload de skills/plugins no agente após instalar. Daqui em diante `ui-ux-pro-max` não é
invocada mais — o restante do fluxo trabalha **em cima** do rascunho, corrigindo.

### 1. `/impeccable init`
Cria `PRODUCT.md` e `DESIGN.md`. Responder com o **produto real** (o que é, público, tom).
Produto inventado → design inventado. Isso molda tudo que vem depois.

### 2. `/impeccable audit` — só diagnóstico, não conserta
Boletim em 5 dimensões (acessibilidade, performance, responsivo, integridade, tipografia/tokens)
com severidade **P0 → P3**. Slop não é só estética: WCAG, SEO e leitores de tela contam.
Sair dele com a lista de "recommended actions" e executar **uma de cada vez**.

### 3. Corrigir em ordem
| Comando | O que faz | Quando |
|---|---|---|
| `/impeccable typeset` | Conserta tipografia, textos quebrados, escala | Primeiro, resolve o mais visível |
| `/impeccable adapt` | Adapta para outro contexto: tamanho de tela, dispositivo, plataforma | Portar desktop → mobile, sistema não-responsivo |
| `/impeccable harden` | Blinda contra uso real: input estranho, erro, idioma longo, conexão ruim, estados vazios | Sempre antes de polish |
| `/impeccable polish` | Refinamento fino. **Não é redesign.** | **Por último** — rodar cedo quebra as coisas |

Depois: `/impeccable audit` de novo e prompts pontuais ("ainda há gradientes soltos e fontes
misturadas; cheque de novo"). Gradientes costumam sobreviver ao primeiro passe.

### 4. Referência visual "no olho" (mais rápido que extrair tokens)
- Fontes: https://dribbble.com, https://dark.design (landings dark), Framer templates.
- Print da referência → colar no agente: *"replique esta estrutura usando as cores, fontes e
  tokens do meu DESIGN.md"*.
- Extrair tokens página-a-página via MCP gasta tempo e tokens; print + polish rende mais.
- Copiar a estrutura crua **sem polir** = slop de outro jeito. Sempre voltar ao passo 3.

### 5. Pesquisa com base real (LazyWeb MCP, https://www.lazyweb.com)
Ferramentas: buscar referências de telas por tipo (pricing, onboarding, paywall…), score,
relatórios, mockups baseados em telas de mercado. Prompt em 3 passos, sem alterar nada até o 3º:
1. *"Busque no LazyWeb referências de pricing page de ferramenta para dev."*
2. *"Desses itens, escolha os 5 que mais mudam a leitura da página, em ordem de impacto.
   Tabela: item · o que a referência faz · o que a minha faz hoje. Não mude nada ainda."*
3. *"Aplique esses 5 itens usando nossos tokens e a fonte do DESIGN.md."*

### 6. Componentes prontos (Shoogle, https://shoogle.dev)
Buscador de blocos shadcn (React/Next): "pricing", "hero section", "landing" etc. Cada bloco
traz código, presets de tokens e um prompt de instalação. Estrela = pago.
- Colar o bloco **quebra** fonte, espaçamento e cores do projeto → depois de colar, rodar
  `/impeccable typeset` + `polish` ou pedir explicitamente: *"use os tokens de cor e fonte da
  minha landing"*.
- Outra stack (Vue, Svelte, HTML puro): pedir adaptação à IA; não é nativo.

### 7. Regras que a web espera
https://interfaces.rauno.me (Web Interface Guidelines): hover, focus, acessibilidade, tipografia,
interação — coisas básicas provadas por pesquisa. Ler antes de dizer que terminou.

## Fluxo resumido (o que funciona)

```
rascunho rápido (ui-ux-pro-max ou tela existente)   ← modelo a ser desmontado
        ↓
referência copiada (print) OU bloco do Shoogle
        ↓
/impeccable init → audit → typeset → adapt → harden → polish
        ↓
audit de novo + prompts pontuais até o detect parar de apontar o óbvio
        ↓
checar interfaces.rauno.me
```

## Checklist antes de entregar UI

- [ ] Se `ui-ux-pro-max` gerou o rascunho, nada dele foi entregue sem passar por audit → polish
- [ ] PRODUCT.md/DESIGN.md descrevem o produto real
- [ ] `audit` sem P0/P1 abertos
- [ ] `polish` rodou por último
- [ ] Nenhum gradiente em headline, nenhum grid-de-pontos de fundo sem motivo, no máximo 2 fontes
- [ ] Componente colado usa os tokens do projeto (fonte, espaçamento, cor)
- [ ] Estados: vazio, erro, loading, texto longo, mobile
- [ ] Focus visível e contraste WCAG AA
