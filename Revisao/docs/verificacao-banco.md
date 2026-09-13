# Verificação do banco

## Inserção válida

A inserção com status `aberto` foi aceita e a consulta retornou o registro com identificador único gerado automaticamente.

```sql
INSERT INTO chamados (titulo, descricao, status)
VALUES ('Acesso bloqueado', 'Não consigo acessar o painel.', 'aberto');
-- Resultado: 1 linha inserida

SELECT id, titulo, status FROM chamados;
-- id | titulo           | status
-- 1  | Acesso bloqueado | aberto
```

## Inserção com status inválido

A inserção com status `cancelado` foi recusada pela restrição de integridade `chamados_status_valido`.

```sql
INSERT INTO chamados (titulo, descricao, status)
VALUES ('Teste', 'Verificar restrição.', 'cancelado');
-- Resultado: ERROR - new row violates check constraint "chamados_status_valido"
```

## Observações

- `NOT NULL` impede campos obrigatórios sem valor.
- `PRIMARY KEY` identifica cada registro de forma única.
- `CHECK` impede estados não previstos pelo domínio.
- O status `em_andamento` é permitido pela restrição.
