from integracao_clientes import adaptar_cliente, ClienteInvalido

externo = {
    "id": 42,
    "full_name": "Ana Souza",
    "branch_code": "SP-01",
    "active": True
}

print(adaptar_cliente(externo))

try:
    adaptar_cliente({"branch_code": "SP-01"})
except ClienteInvalido as erro:
    print(type(erro).__name__, str(erro))
