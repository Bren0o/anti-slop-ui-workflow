# Exemplos — mesmo prompt, com e sem a skill

Prompt idêntico para dois agentes (Claude, mesma sessão, 28/08/2026):
> "Crie uma landing page em um único HTML para uma ferramenta de CI chamada FlowBase (pipelines de CI/CD para times pequenos)."

| | `flowbase-sem-skill/` | `flowbase-com-skill/` |
|---|---|---|
| Instrução extra | nenhuma ("faça como normalmente faria") | ler e seguir `skills/anti-slop-ui-workflow/SKILL.md` + references; sem browser, sem Impeccable, sem Stitch/v0/Mobbin |
| `npx impeccable detect` 1280×800 | **45** anti-padrões | **9** → após polish (3 ajustes CSS) **0** |
| `detect --viewport 390x844` | **42** | **0** |
| Categorias (sem skill) | ai-color-palette 27 · kicker-above-heading 5 · icon-tile-stack 4 · line-length 3 · thin-border-wide-shadow 2 · dark-glow 2 · overused-font 1 · blinking-cursor 1 | low-contrast 5 (cinza #7B838B a 3.6:1) · cramped-padding 3 · all-caps-body 1 |
| Estrutura | navbar → hero texto-esq/terminal-dir → 6 cards com ícone → 3 passos → métricas → 3 planos (meio destacado) → depoimento → FAQ → CTA | hero + run view com **job falhando** → como funciona (`flowbase.yml`) → **tabela comparativa** → 3 números → 2 planos sem "mais popular" → form |
| Fontes | Inter/sistema + mono | IBM Plex Sans + Plex Mono |
| Cor | dark + verde-água neon + glows | claro, tinta preta, um teal |

## Terceira rodada: híbrido (`flowbase-hibrido/`)

Feedback do usuário sobre a versão com skill: "sendo sincero não vi diferença" — correta, mas sem graça. `detect` em 0 não é entrega.
Pedido: mesclar a energia da A com a disciplina da B, **partindo de uma direção estética escolhida** (`frontend-aesthetic-direction`).

Direção: "folha de especificação industrial" — papel frio, tinta quase preta, uma cor de carimbo (vermelhão), Archivo Expanded 900 + JetBrains Mono, raio 0, sem sombra, seções numeradas `§ 01…04`.
De A: headline gigante com voz, run/log como peça central, ritmo de seções, CTA em bloco sólido. De B: job falhando com stack trace, tabela comparativa, 2 planos, foco/hover/reduced-motion, contraste AA.

`detect` desktop: **1** (`oversized-h1` — intencional, é a identidade). Mobile: 3 → **0** após `min-width: 0` nos filhos de grid (log/YAML com `overflow-x:auto` empurravam a grade além da tela — bug real que o detector achou).

Lição para a skill: sem referência ou direção estética, tirar o slop entrega uma página correta e anônima. A régua final é o olho de quem pediu.

Ajuste após feedback "no Windows fica tudo estourado": h1 96→60 px, h2 52→38, números 56→40, preços 64→44 (a 125 % de escala, 96 px vira cartaz). `flowbase-paletas/` é a prévia de paletas que a skill agora manda mostrar antes de gerar.

Arquivos:
- `flowbase-sem-skill/index.html` + `detect.txt`
- `flowbase-hibrido/index.html` + `detect.txt` (1 achado intencional)
- `flowbase-com-skill/index-antes-do-polish.html` + `detect-antes-do-polish.txt` (9 achados) e `index.html` (após polish, 0 achados)

Leitura honesta: a versão sem skill é vistosa — e é exatamente o site de dev-tool que toda IA gera. A com skill muda **estrutura** (não só cor), mostra produto real e sobra só ajuste fino. O que a skill delega a ferramentas (Impeccable `audit`/`polish`, Mobbin, Stitch) não foi usado neste teste; com elas o resultado tende a ser melhor, não pior.

Reproduzir: servir a pasta (`python -m http.server 8765`) e rodar `npx impeccable detect http://127.0.0.1:8765/<pasta>/index.html`.
