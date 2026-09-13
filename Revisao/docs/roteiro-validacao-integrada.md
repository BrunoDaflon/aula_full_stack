# Roteiro de validação integrada

| Cenário | Entrada ou ação | Resultado HTTP ou técnico esperado | Resultado visual esperado | Evidência |
|---|---|---|---|---|
| Cadastro válido | Enviar título, descrição e prioridade `alta` | `201 Created`; chamado persistido | Confirmação de cadastro e item na lista | Captura da tela e resposta HTTP |
| Prioridade inválida | Enviar prioridade `urgente` | `400 Bad Request`; nenhum chamado criado | Mensagem orientando prioridades aceitas | Resposta HTTP e lista sem novo item |
| Consulta de chamados | Abrir ou atualizar a tela | `200 OK`; lista JSON, vazia ou preenchida | Lista ou mensagem de lista vazia | Captura e resposta HTTP |
| Serviço externo indisponível | Simular timeout ou resposta inesperada | Falha tratada pelo cliente de integração | Mensagem de indisponibilidade, sem detalhe técnico | Registro do cenário e captura |
| Carregamento inicial | Abrir a interface antes da resposta | Requisição em andamento | Mensagem de carregamento antes da lista | Captura ou vídeo curto |

## Execução

1. Iniciar banco e aplicar o script `banco/001_criar_tabela_chamados.sql`.
2. Iniciar a API com `uvicorn main:app --reload`.
3. Iniciar a interface com `python -m http.server 5500`.
4. Executar cada cenário e salvar as evidências no repositório.
5. Registrar defeitos encontrados e a decisão de correção.
