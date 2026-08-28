---
name: anti-slop-ui-workflow
description: Fluxo completo para tirar "AI slop" de interfaces geradas por IA — auditar com Impeccable (detect/init/audit/typeset/adapt/harden/polish), puxar referências visuais (Dribbble, dark.design, LazyWeb MCP), montar com componentes prontos (Shoogle/shadcn) e polir de volta aos tokens do projeto. Use quando o usuário pedir landing page, hero, pricing, dashboard ou qualquer UI hi-fi, quando disser que a tela "parece feita por IA", ou antes de entregar frontend gerado por agente. Regra de entrada: já tem layout → refina sem ui-ux-pro-max; não tem → cria com ui-ux-pro-max e depois refina.
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

Catálogo nomeado com o motivo de cada padrão: https://impeccable.style/slop — escrito por
Paul Bakaus (criador do jQuery UI, ex-Google for Creators). Quando a skill diz "isso é slop",
a régua é a dele, não gosto pessoal: cada anti-padrão vem com o porquê. Cite o motivo ao
apontar um problema, não só o nome do padrão.
Detector automático: `npx impeccable detect https://site.com` (o comando acha mais que a
extensão Chrome — inclui padrões de **código**, não só visuais). É baseado em padrões, **não é
exato**: acha "slop" até no GitHub e em README, porque padrão antigo ≠ padrão ruim. Slop é a
**combinação** de padrões, não um isolado — usar o olho para confirmar cada apontamento.

## Porta de entrada — primeira pergunta, sempre

**Já existe layout?**

| Resposta | Caminho |
|---|---|
| **Sim** (tela legada, vibe-coded, v0/Lovable/Gemini, Figma implementado) | Vai direto para o **refinamento** (passo 1 em diante). **Não** invocar `ui-ux-pro-max` — ela só adicionaria slop em cima do que já existe. |
| **Não** (página em branco) | **Criar primeiro com `ui-ux-pro-max`** (passo 0), depois **refinar** (passos 1–7). |

Se não estiver claro, perguntar ao usuário antes de gerar qualquer coisa.

## Fluxo — na ordem, sem pular

### 0. Criar o rascunho com `ui-ux-pro-max` (só quando NÃO existe layout)
Gerar a tela com um prompt curto, como no vídeo (`landing page de ferramenta de CI chamada
FlowBase`). Regras do rascunho:
- Prompt **curto**. Quanto mais especificação, mais genérico o resultado dessa skill.
- Aceitar que vai sair slop: gradiente no título, card flutuando à direita, três cards. É o
  ponto de partida para medir e corrigir, não a entrega.
- Rodar uma vez só. Não ficar iterando com a Pro Max — a iteração é do Impeccable.

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

Ao terminar, o `init` sugere os próximos passos. Há **dois caminhos** a partir daqui:

| Caminho | Quando | Comandos |
|---|---|---|
| **Rápido** (o que o próprio Impeccable recomenda) | Página simples, poucos problemas, quer resultado logo | `/impeccable document` → `/impeccable critique` → `/impeccable polish` |
| **Auditável** (o do vídeo) | Página com muito slop, quer ver todos os problemas e corrigir um a um com rastro | `/impeccable audit` → passos 2–3 abaixo |

Na dúvida, rodar `audit` primeiro só para medir; se vier pouca coisa, seguir o caminho rápido.

### 2. `/impeccable audit` — só diagnóstico, não conserta
Boletim em 5 dimensões (acessibilidade, performance, responsivo, integridade, tipografia/tokens)
com severidade **P0 → P3**. Slop não é só estética: WCAG, SEO e leitores de tela contam.
Sair dele com a lista de "recommended actions" e executar **uma de cada vez**.

### 3. Corrigir em ordem
| Comando | O que faz | Quando |
|---|---|---|
| `/impeccable typeset` | Conserta tipografia, textos quebrados, escala | Primeiro, resolve o mais visível |
| `/impeccable adapt` | Adapta para outro contexto: tamanho de tela, dispositivo, plataforma | Portar desktop → mobile, sistema não-responsivo |
| `/impeccable harden` | Blinda contra uso real: input estranho, erro, idioma longo, conexão ruim, estados vazios. Conferir com as seções Interatividade/Toque/Acessibilidade de `references/web-interface-guidelines.md` | Sempre antes de polish |
| `/impeccable polish` | Refinamento fino. **Não é redesign.** Conferir com Tipografia/Movimento/Design de `references/web-interface-guidelines.md` | **Por último** — rodar cedo quebra as coisas |

**Após cada passe: refresh e olhar a tela.** Cada comando pode introduzir regressão pequena
(texto colado, espaçamento quebrado) — checar antes de rodar o próximo. Depois: `/impeccable
audit` de novo e prompts pontuais ("ainda há gradientes soltos e fontes misturadas; cheque de
novo"). Gradientes costumam sobreviver ao primeiro passe.

**Regra do loop:** tudo que entra de fora — bloco do Shoogle, referência copiada, componente
gerado — passa por `audit` → correção → `audit` outra vez. "Copiou? Melhora com Impeccable.
Viu o audit errado? Melhora com Impeccable." O fluxo não tem fim declarado; para quando o
audit não traz P0/P1 e o detect só aponta o que você decidiu manter.

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
Buscador de blocos shadcn (React/Next): "pricing", "hero section", "landing", categoria
*Feature blocks*. Cada bloco traz **três artefatos**: código (copiar direto), *presets* de
tokens de design (adotar só se quiser os tokens do bloco — senão ignorar e manter o DESIGN.md)
e um **prompt** de instalação (o caminho mais rápido: colar no agente). Estrela = pago.
Blocos "flexíveis" (várias estruturas de hero no mesmo componente) rendem mais que os fixos.
- Colar o bloco **quebra** fonte, espaçamento e cores do projeto (no vídeo: cor manteve em
  parte, fonte e espaçamento não) → pedir já no prompt de instalação: *"instale usando os
  tokens de cor e fonte do meu DESIGN.md"*, e depois `/impeccable audit` → `typeset` → `polish`
  (regra do loop).
- Outra stack (Vue, Svelte, HTML puro): pedir adaptação à IA; não é nativo.

### 7. Regras que a web espera (Web Interface Guidelines)
**Ler `references/web-interface-guidelines.md`** (checklist condensado de
https://interfaces.rauno.me, Rauno Freiberg) e percorrer todas as seções antes de dizer que
terminou: Interatividade, Tipografia, Movimento, Toque, Performance, Acessibilidade, Design.
São regras provadas por uso real, não gosto — e cobrem o que o Impeccable não vê: label que
não foca o input, hover preso no touch, `font-size < 16px` dando zoom no iOS, tooltip em
botão desabilitado, foco com `outline` cortando o `border-radius`, animação > 200 ms.
Cada item ❌ vira P1 (acessibilidade/toque) ou P2 (resto) e volta para `harden`/`polish`.

## Setup das ferramentas (fazer uma vez por projeto)

Antes de rodar o fluxo, verificar o que já está instalado (`/skills`, `/mcp`) e configurar o que
faltar. Nunca gravar token em arquivo versionado — `.mcp.json` com token vai no `.gitignore`.

### Impeccable (skill + hooks)
```bash
npx impeccable install      # responder: "project" (não global) · hooks: sim
```
Hooks "sim" porque o detect passa a rodar sozinho a cada mudança — e ver o apontamento
repetidas vezes é como se aprende o que é slop (gosto se treina; não há skill que faça 100%).
Depois: `/reload-plugins` (ou reiniciar o agente) e confirmar que `/impeccable ...` aparece.
Detector standalone (sem instalar): `npx impeccable detect <url>` · extensão Chrome "Impeccable".

### LazyWeb MCP (pesquisa de referência com base real) — https://www.lazyweb.com
1. Obter o token com o `curl` publicado na descrição do vídeo/site (devolve um Bearer token):
   ```bash
   curl -X POST https://www.lazyweb.com/<endpoint-de-token>   # ver descrição do vídeo
   ```
2. Registrar o MCP no Claude Code trocando `<TOKEN>` pelo valor recebido (sem espaços):
   ```bash
   claude mcp add --transport http lazyweb https://www.lazyweb.com/<mcp-endpoint> \
     --header "Authorization: Bearer <TOKEN>"
   ```
3. `/reload-plugins` → `/mcp` → `lazyweb` deve listar tools como *search/report/score/mockup*.
Versão gratuita tem base menor; as pagas trazem mais telas. Prompt de uso: ver passo 5.

### Shoogle (blocos shadcn) — https://shoogle.dev
Não tem instalação: buscar o bloco, copiar o **prompt** (ou o código) e colar no agente. O prompt
instala as dependências via shadcn CLI; se pedir para sobrescrever `components/ui/*`, aceitar
só se o projeto ainda não customizou esses arquivos. React/Next nativo; outra stack → pedir
adaptação.

### Referências visuais
- https://dribbble.com · https://dark.design (dark) · templates do Framer → print → colar.
- https://interfaces.rauno.me — ler antes do checklist final.

### Modelo local (opcional)
Para rodar `detect`/`audit` com modelo local, checar o que a máquina aguenta em
https://canirunai.kc1t.com antes de configurar Ollama/LM Studio.

## Fluxo resumido (o que funciona)

```
Já tem layout?
  ├─ sim → segue direto (sem ui-ux-pro-max)
  └─ não → cria com ui-ux-pro-max (1x, prompt curto)
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
- [ ] Focus visível (box-shadow, não outline) e contraste WCAG AA
- [ ] `references/web-interface-guidelines.md` percorrido inteiro — sem ❌ em Acessibilidade e Toque
