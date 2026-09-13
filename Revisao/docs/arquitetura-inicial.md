# Arquitetura inicial — Sistema de chamados

## Fluxo de abertura de chamado

Pessoa usuária
  → Front-end (coleta dados do formulário)
  → API / Back-end (valida dados e aplica regras)
  → Banco de dados (persiste o chamado)
  → API / Back-end (confirma a operação)
  → Front-end (exibe confirmação ou erro)
  → Pessoa usuária

## Responsabilidades

| Componente | Responsabilidade principal | Não deve concentrar |
|---|---|---|
| Front-end | Exibir formulário, coletar dados e mostrar feedback | Regras críticas de negócio e persistência direta |
| API / Back-end | Receber solicitações, validar dados, aplicar regras e coordenar operações | Detalhes de apresentação visual |
| Banco de dados | Armazenar e recuperar chamados persistentemente | Mensagens de interface e fluxo HTTP |
| Serviço externo | Oferecer uma capacidade de outro sistema, quando necessário | Regras centrais do sistema de chamados |

## Fluxo prioritário

1. A pessoa cliente preenche título, descrição e prioridade.
2. O front-end envia os dados à API.
3. O back-end valida os dados e verifica a prioridade permitida.
4. O banco persiste o chamado.
5. O back-end devolve o resultado.
6. O front-end informa o sucesso ou o erro.
