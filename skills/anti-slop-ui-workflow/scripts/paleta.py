#!/usr/bin/env python3
"""Prévia de paletas para a skill anti-slop-ui-workflow.

Uso:
  python paleta.py                 # imprime as paletas no terminal (ANSI 24-bit) e abre o HTML no navegador padrão
  python paleta.py --no-open       # só terminal
  python paleta.py --html saida.html  # gera o HTML a partir das paletas deste arquivo e abre

Edite SÓ a lista PALETAS. Mesmo formato do references/paleta-preview.html.
Funciona em Claude Code, Codex, Cursor — qualquer agente que rode shell.
"""
import argparse, json, os, sys, webbrowser, pathlib

PROJETO = "Nome do projeto"
PALETAS = [
    {"nome": "1 · Folha industrial", "mood": "papel frio, carimbo, denso",
     "bg": "#F3F2EE", "surface": "#FFFFFF", "ink": "#16171A", "ink2": "#5B5D63", "brand": "#C43A14",
     "ok": "#1F7A3E", "err": "#B3261E", "warn": "#9A6700",
     "display": "'Archivo', sans-serif", "text": "'IBM Plex Sans', sans-serif", "mono": "'IBM Plex Mono', monospace"},
    {"nome": "2 · Editorial", "mood": "serifa de display, claro, calmo",
     "bg": "#FBFAF7", "surface": "#FFFFFF", "ink": "#1C1B18", "ink2": "#66625A", "brand": "#1F4B99",
     "ok": "#2E7D4F", "err": "#B42318", "warn": "#B54708",
     "display": "'Instrument Serif', serif", "text": "'Source Sans 3', sans-serif", "mono": "'JetBrains Mono', monospace"},
    {"nome": "3 · Painel escuro sóbrio", "mood": "dark sem neon, cinza quente, âmbar",
     "bg": "#141416", "surface": "#1D1D20", "ink": "#EDEDEA", "ink2": "#A3A39E", "brand": "#E0A030",
     "ok": "#5BBF7A", "err": "#F26D5B", "warn": "#E0A030",
     "display": "'Manrope', sans-serif", "text": "'DM Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    {"nome": "4 · Verde de fábrica", "mood": "claro, verde escuro como marca, técnico",
     "bg": "#F4F6F3", "surface": "#FFFFFF", "ink": "#141A16", "ink2": "#5A665E", "brand": "#0F5C3A",
     "ok": "#0F5C3A", "err": "#A8321F", "warn": "#8A6100",
     "display": "'DM Sans', sans-serif", "text": "'DM Sans', sans-serif", "mono": "'IBM Plex Mono', monospace"},
]
CHAVES = ["bg", "surface", "ink", "ink2", "brand", "ok", "err", "warn"]


def rgb(hexa):
    h = hexa.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def bloco(hexa, largura=10):
    r, g, b = rgb(hexa)
    return f"\x1b[48;2;{r};{g};{b}m{' ' * largura}\x1b[0m"


def terminal():
    if os.name == "nt":
        os.system("")  # habilita ANSI no conhost/Windows Terminal
    print(f"\nPaletas para: {PROJETO}\n")
    for p in PALETAS:
        print(f"{p['nome']}  —  {p['mood']}")
        print("  " + " ".join(bloco(p[k]) for k in CHAVES))
        print("  " + " ".join(f"{k:<10}" for k in CHAVES))
        print("  " + " ".join(f"{p[k]:<10}" for k in CHAVES))
        fontes = " + ".join(p[k].split(",")[0].strip("'") for k in ("display", "text", "mono"))
        # amostra: texto na tinta sobre o fundo, botão na cor de marca
        br, bg_, bb = rgb(p["bg"]); ir, ig, ib = rgb(p["ink"]); mr, mg, mb = rgb(p["brand"])
        print(f"  \x1b[48;2;{br};{bg_};{bb}m\x1b[38;2;{ir};{ig};{ib}m  Pipelines que o time inteiro consegue ler.  "
              f"\x1b[48;2;{mr};{mg};{mb}m\x1b[38;2;255;255;255m Ação \x1b[0m  {fontes}\n")
    print("Responda com o número da paleta (ou diga o que mudar em uma delas).")


def html(saida):
    modelo = pathlib.Path(__file__).resolve().parent.parent / "references" / "paleta-preview.html"
    src = modelo.read_text(encoding="utf-8")
    ini = src.index("const PROJETO")
    fim = src.index("// ===== FIM =====")
    novo = f'const PROJETO = {json.dumps(PROJETO, ensure_ascii=False)};\nconst PALETAS = {json.dumps(PALETAS, ensure_ascii=False, indent=2)};\n'
    out = pathlib.Path(saida)
    out.write_text(src[:ini] + novo + src[fim:], encoding="utf-8")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-open", action="store_true")
    ap.add_argument("--html", default="paletas-preview.html")
    a = ap.parse_args()
    terminal()
    out = html(a.html)
    print(f"HTML: {out}")
    if not a.no_open:
        webbrowser.open(out.as_uri())  # navegador padrão do usuário (file:// funciona aqui)
