# Contrato inicial — Chamados

## Listar chamados

- **Método:** `GET`
- **URI:** `/chamados`
- **Sucesso:** `200 OK`

```json
[
  {
    "id": 1,
    "titulo": "Acesso bloqueado",
    "descricao": "Não consigo acessar o painel.",
    "prioridade": "alta",
    "status": "aberto"
  }
]
```

## Criar chamado

- **Método:** `POST`
- **URI:** `/chamados`
- **Cabeçalho:** `Content-Type: application/json`
- **Sucesso:** `201 Created`

```json
{
  "titulo": "Acesso bloqueado",
  "descricao": "Não consigo acessar o painel.",
  "prioridade": "alta"
}
```

## Erro de validação

- **Status:** `400 Bad Request`

```json
{
  "erro": "DADOS_INVALIDOS",
  "mensagem": "A prioridade informada não é aceita.",
  "campos": {
    "prioridade": "Use baixa, media ou alta."
  }
}
```
