# Revisão do fluxo de atualização de status

## Fluxo recebido

Pessoa usuária → Front-end → Banco de dados → `/atualizarStatus/7`

## Fluxo corrigido

Pessoa usuária → Front-end → API / Back-end → Banco de dados → API / Back-end → Front-end

A interface não acessa o banco diretamente. O back-end valida a solicitação, aplica regras do domínio e coordena a persistência.

## Operação HTTP

- **Método:** `PATCH`
- **URI:** `/chamados/7`
- **Cabeçalho:** `Content-Type: application/json`

```json
{
  "status": "em_andamento"
}
```

- **Resposta de sucesso:** `200 OK`

```json
{
  "id": 7,
  "titulo": "Acesso bloqueado",
  "descricao": "Não consigo acessar o painel.",
  "prioridade": "alta",
  "status": "em_andamento"
}
```
