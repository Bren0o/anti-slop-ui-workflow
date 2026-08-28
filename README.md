# anti-slop-ui-workflow

Skill para Claude Code / Codex / Cursor que tira o "AI slop" de interfaces geradas por IA.

Uma base fixa de regras (como a UI/UX Pro Max) faz toda landing page sair igual: gradiente no título, três cards, hero texto-esquerda/imagem-direita. Esta skill segue o fluxo do vídeo: usa esse rascunho genérico apenas como **modelo a ser desmontado** e guia o agente por **auditoria → correção → referência real → componentes prontos → polimento**:

0. Rascunho rápido (UI/UX Pro Max ou tela existente) — descartável, nunca a entrega
1. **Impeccable** (`init → audit → typeset → adapt → harden → polish`, sempre nessa ordem)
2. Referência visual por print (Dribbble, dark.design) aplicada com os tokens do projeto
3. Pesquisa com base real via **LazyWeb MCP** (prompt em 3 passos)
4. Blocos prontos do **Shoogle** (shadcn) + re-polish para respeitar fonte/espaçamento/cor
5. Checklist final com as **Web Interface Guidelines** (interfaces.rauno.me)

Baseada no vídeo ["Remova Essa Skill de UI do Seu Projeto AGORA"](https://www.youtube.com/watch?v=GdzswgxcqPg).

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
- `npx impeccable install` no projeto (responda **project**, não global) — https://impeccable.style
- LazyWeb MCP — https://www.lazyweb.com
- Shoogle — https://shoogle.dev

## Estrutura
```
skills/
└── anti-slop-ui-workflow/
    └── SKILL.md
```

## Licença
MIT
