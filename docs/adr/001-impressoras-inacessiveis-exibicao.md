# ADR 001 — Exibição de impressoras inacessíveis no dashboard

- **Status:** Aceito
- **Data:** 2026-05-21
- **Issue:** [#2 — Comportamento do dashboard quando uma impressora está inacessível](https://github.com/edpittol/aula-do-roveda/issues/2)

## Contexto

Quando o scraper tenta consultar o nível de toner de uma impressora e ela não responde (timeout, connection refused, IP incorreto), retorna um valor sentinela de "inacessível". Precisávamos definir o que o dashboard exibe nesse caso antes de implementar o template HTML e a lógica de filtragem no Flask route.

Quatro opções foram avaliadas na issue #2.

## Decisão

**Opção B — Exibir na lista com status "Inacessível".**

A impressora aparece normalmente na lista de resultados, mas com o campo de nível de toner substituído pelo rótulo "Inacessível" (em vez de um valor numérico ou percentual).

## Justificativa

- Garante visibilidade total: o analista sabe exatamente quais impressoras foram verificadas e quais não responderam.
- Mantém o layout simples — sem seções extras nem lógica de colapso.
- Falha explícita é preferível a falha silenciosa (Opção A), pois o analista precisa saber que uma impressora não foi verificada naquele ciclo.
- Complexidade menor que a Opção C (seção separada), suficiente para o caso de uso atual.

## Consequências

- O template HTML deve tratar o campo de toner como opcional: renderizar "Inacessível" quando o valor sentinela for detectado.
- A lógica de ordenação/filtragem no Flask route deve incluir as impressoras inacessíveis, posicionando-as adequadamente na lista (ex.: ao final).
- Se o número de impressoras inacessíveis crescer, pode ser revisado para Opção C no futuro.
