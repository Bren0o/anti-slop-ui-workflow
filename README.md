# anti-slop-ui-workflow

Skill para Claude Code / Codex / Cursor que tira o "AI slop" de interfaces geradas por IA.

Uma base fixa de regras (como a UI/UX Pro Max) faz toda landing page sair igual: gradiente no título, três cards, hero texto-esquerda/imagem-direita. Esta skill não gera telas — ela **dá gosto** ao agente: ensina a ver o que está ruim e guia pelo fluxo dos vídeos, **na ordem certa**:

**Porta de entrada** — *Já tem layout?* Sim → loop Impeccable direto, sem UI/UX Pro Max. Não → passos 1–4. *Tem referência?* Sem → rascunho visual com Gemini (Stitch/Antigravity); com print → Claude no repo com os tokens do projeto.

1. **Briefing visual** — direção estética e densidade escolhidas pelo usuário (uma rodada de `AskUserQuestion`), tela pronta em vez de prévia de paleta, teto de tamanho para escala do Windows (h1 ≤ 60 px, testar 1366×768 e 390×844)
2. **Referência real** — **Mobbin → Pinterest → Dribbble** (cada fonte tem um papel), um elemento por vez, aplicado com os tokens do projeto; pesquisa via **LazyWeb MCP** (prompt em 3 passos); blocos prontos **Shoogle / Aceternity / 21st.dev**; **checklist de prompt injection** antes de colar qualquer prompt público
3. **Rascunho** — print + Google Stitch / v0; UI/UX Pro Max só como fallback, uma vez, prompt curto, e nunca sem Impeccable para desmontar
4. **Loop Impeccable** — `init` → caminho rápido (`document → critique → polish`) ou auditável (`audit → typeset → adapt → harden → polish`); qualquer P0/P1 → auditável; olhar a tela após cada passe; tudo que entra de fora passa por `audit` de novo
5. **Web Interface Guidelines** (interfaces.rauno.me) — checklist final

Mais: tabela de **erros comuns** (polish primeiro, parar no `detect = 0`, agente escolhendo direção sozinho…), skills locais encadeadas (impeccable, ai-slop-check, polish-pass, critique-*, accessibility-audit…) e checklist de entrega.

Baseada nos vídeos ["Remova Essa Skill de UI do Seu Projeto AGORA"](https://www.youtube.com/watch?v=GdzswgxcqPg) e ["Todo Site Feito com IA É Igual (e Como Fugir Disso)"](https://www.youtube.com/watch?v=I8_RP_BJVLk).

## Instalação

### Claude Code (global)
```bash
git clone https://github.com/Bren0o/anti-slop-ui-workflow.git
cp -r anti-slop-ui-workflow/skills/anti-slop-ui-workflow ~/.claude/skills/
```
Windows (PowerShell):
```powershell
git clone https://github.com/Bren0o/anti-slop-ui-workflow.git
Copy-Item -Recurse anti-slop-ui-workflow\skills\anti-slop-ui-workflow $env:USERPROFILE\.claude\skills\
```

### Por projeto
Copie `skills/anti-slop-ui-workflow/` para `.claude/skills/` na raiz do projeto.

A skill é ativada automaticamente quando você pede landing page, hero, pricing, dashboard ou qualquer UI hi-fi — ou invoque com `/anti-slop-ui-workflow`.

## Pré-requisitos (opcionais, mas é onde a skill brilha)
A skill traz uma seção **Setup das ferramentas** com os comandos de cada uma:
- Impeccable: `npx impeccable install` (responda **project**, aceite os hooks) — https://impeccable.style
- LazyWeb MCP (opcional): `curl -s -X POST https://www.lazyweb.com/api/mcp/install-token` → `claude mcp add --transport http --scope user lazyweb https://www.lazyweb.com/mcp --header "Authorization: Bearer SEU_TOKEN"` — https://www.lazyweb.com (nunca commitar o token)
- Shoogle: sem instalação, copia o prompt do bloco e cola no agente — https://shoogle.dev
- Desenhar antes de codar: Google Stitch (https://stitch.withgoogle.com, ~300 créditos/dia), v0 (https://v0.app, US$ 5/mês), Subframe (https://subframe.com, 10 pág/dia)
- Referências: https://mobbin.com · https://pinterest.com · https://dribbble.com · https://dark.design
- Componentes: https://ui.aceternity.com · https://21st.dev (público — ler o prompt antes de colar)
- Web Interface Guidelines — https://interfaces.rauno.me

## Prova: mesmo prompt, com e sem a skill
`npx impeccable detect` na landing "FlowBase" gerada pelo mesmo modelo: **45 anti-padrões sem a skill → 9 com a skill → 0 após polish** (mobile: 42 → 0). Terceira rodada, híbrido com direção estética própria: 1 achado intencional (h1 gigante), mobile 0 — e finalmente com identidade. HTMLs, relatórios e comparação em [`examples/`](examples/README.md).

## Estrutura
```
skills/
└── anti-slop-ui-workflow/
    ├── SKILL.md
    └── references/
        ├── web-interface-guidelines.md              # checklist condensado de interfaces.rauno.me
        └── ferramentas-de-referencia-e-geracao.md   # Mobbin/Pinterest/Dribbble, Stitch/v0/Subframe, modelo por tarefa, catálogos, prompt injection
examples/                                            # FlowBase com/sem skill + relatórios do detect
```

## Licença
MIT
