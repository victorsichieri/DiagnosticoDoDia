#!/usr/bin/env python3
"""Confere casos.json (e opcionalmente um lote em pendentes/) antes de publicar.

Uso:
  python3 scripts/validar.py                 # valida casos.json
  python3 scripts/validar.py pendentes/x.json  # valida um lote junto com o banco atual
"""
import json, sys, re, unicodedata
from datetime import date

NIVEIS = {"facil", "inter", "dificil", "mdificil"}

def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", s.lower())).strip()

def checar(casos, rotulo):
    erros, avisos = [], []
    ids, slots, dx_nivel = set(), set(), {}
    for c in casos:
        cid = c.get("id", "?")
        for campo in ("id", "data", "nivel", "diagnostico", "sinonimos", "dicas", "comentario"):
            if campo not in c:
                erros.append(f"{cid}: falta o campo '{campo}'")
        if cid in ids:
            erros.append(f"{cid}: id repetido")
        ids.add(cid)
        if c.get("nivel") not in NIVEIS:
            erros.append(f"{cid}: nível inválido '{c.get('nivel')}'")
        try:
            date.fromisoformat(c.get("data", ""))
        except ValueError:
            erros.append(f"{cid}: data inválida '{c.get('data')}'")
        slot = (c.get("data"), c.get("nivel"))
        if slot in slots:
            erros.append(f"{cid}: já existe caso para {slot[1]} em {slot[0]}")
        slots.add(slot)
        dicas = c.get("dicas", [])
        if len(dicas) != 5 or not all(isinstance(d, str) and len(d) > 15 for d in dicas):
            erros.append(f"{cid}: precisa de exatamente 5 dicas com texto")
        nomes = [norm(c.get("diagnostico", ""))] + [norm(s) for s in c.get("sinonimos", []) if len(norm(s)) >= 5]
        for i, d in enumerate(dicas[:4]):
            nd = f" {norm(d)} "
            for n in nomes:
                if n and f" {n} " in nd:
                    erros.append(f"{cid}: a dica {i + 1} entrega a resposta ('{n}')")
        chave = (c.get("nivel"), norm(c.get("diagnostico", "")))
        if chave in dx_nivel:
            avisos.append(f"{cid}: diagnóstico repetido no mesmo nível (também em {dx_nivel[chave]})")
        dx_nivel[chave] = cid
    print(f"{rotulo}: {len(casos)} casos, {len(erros)} erro(s), {len(avisos)} aviso(s)")
    for e in erros: print("  ERRO  ", e)
    for a in avisos: print("  aviso ", a)
    return not erros

base = json.load(open("casos.json", encoding="utf-8"))
casos = base["casos"]
if len(sys.argv) > 1:
    lote = json.load(open(sys.argv[1], encoding="utf-8"))
    casos = casos + (lote["casos"] if isinstance(lote, dict) else lote)
ok = checar(casos, sys.argv[1] if len(sys.argv) > 1 else "casos.json")
sys.exit(0 if ok else 1)
