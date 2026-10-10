# Regras para gerar novos casos

Estas regras valem para cada lote semanal. O lote nunca vai direto para o jogo: ele entra por um Pull Request que o Victor revisa e aprova.

## O que gerar
- 7 casos por nível (facil, inter, dificil, mdificil) = 28 casos, um por dia.
- Datas: os 7 dias seguintes à última data já presente em `casos.json`.
- Não repetir um diagnóstico que já esteja no mesmo nível. Evitar repetir em qualquer nível nos últimos 60 dias.

## Formato de cada caso
```json
{
  "id": "nivel-slug-do-diagnostico",
  "data": "AAAA-MM-DD",
  "nivel": "facil | inter | dificil | mdificil",
  "diagnostico": "Nome completo em português",
  "sinonimos": ["siglas", "nomes alternativos", "sem acento tudo bem"],
  "dicas": ["1", "2", "3", "4", "5"],
  "comentario": "Ponto-chave de 1 a 2 frases: o achado decisivo e a conduta principal.",
  "revisado": false
}
```
`revisado` sai como `false`. O jogo ignora casos não revisados. Ao aprovar o PR, os casos aprovados passam para `true`.

## Como escrever as dicas
1. Dado demográfico e queixa principal, vaga o bastante para caber em vários diagnósticos.
2. História que estreita o diferencial.
3. Antecedentes, fatores de risco ou evolução.
4. Exame físico característico.
5. Exame complementar decisivo, quase patognomônico.

- Nenhuma das 4 primeiras dicas pode conter o nome do diagnóstico ou um sinônimo.
- Usar unidades e valores brasileiros (mg/dL, mmHg, irpm, °C) e linguagem de pronto-socorro.
- Conteúdo de acordo com diretrizes atuais (SBC, AHA, SBPT, Ministério da Saúde). Na dúvida sobre um dado, não use o caso.

## Dificuldade
- facil: quadros clássicos de UPA (IAM, AVC, PAC, apendicite, CAD).
- inter: emergências que exigem raciocínio (TEP, dissecção, tamponamento, ectópica).
- dificil: clínica e especialidades cobradas em residência (endócrino, reumato, neuro).
- mdificil: diagnósticos raros com achado patognomônico (Whipple, Wilson, porfiria).

## Sinônimos
Incluir siglas, nomes epônimos, formas com e sem "doença de"/"síndrome de", e variações que um médico digitaria na pressa. Não incluir termos amplos demais que aceitariam um diagnóstico diferente.

## Antes de abrir o PR
Rodar `python3 scripts/validar.py` e corrigir todo ERRO.
