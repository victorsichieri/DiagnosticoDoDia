# Diagnóstico do Dia

Jogo de casos clínicos no estilo Wordle. Um caso por dia em quatro níveis (Fácil, Intermediário, Difícil e Muito difícil). A cada erro, uma nova dica; são 5 chances.

## Como funciona
- `index.html`: o jogo inteiro.
- `casos.json`: o banco de casos, cada um com a data em que vira o caso do dia. Dias sem caso agendado reaproveitam casos antigos do mesmo nível.
- Treino: mostra os casos cujo dia já passou e os casos sem data (`"data": null`, só de treino). O caso de hoje e os futuros nunca aparecem no Treino.
- `manifest.webmanifest` e `sw.js`: permitem instalar no celular e jogar offline.
- `scripts/validar.py`: confere o banco (campos, datas, dicas que entregam a resposta, repetições).
- `GERAR_CASOS.md`: regras para escrever novos casos.

## Instalar no celular
Abra o link do GitHub Pages:
- iPhone (Safari): Compartilhar → Adicionar à Tela de Início.
- Android (Chrome): menu ⋮ → Instalar app.

## Novos casos
Toda semana um lote de 28 casos chega como Pull Request, com `revisado: false`. Revise, corrija se precisar, troque para `true` e aprove o merge. O jogo só mostra casos revisados.

Conteúdo educacional; não substitui avaliação clínica.
