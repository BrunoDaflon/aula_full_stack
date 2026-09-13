import requests


class ClienteIndisponivel(Exception):
    pass


class ClienteInvalido(Exception):
    pass


def adaptar_cliente(dados_externos):
    if "full_name" not in dados_externos:
        raise ClienteInvalido("Resposta externa sem nome da pessoa cliente.")

    return {
        "nome_cliente": dados_externos["full_name"],
        "codigo_unidade": dados_externos.get("branch_code"),
        "cliente_ativo": dados_externos.get("active", False)
    }


def buscar_cliente_interno(base_url, cliente_id):
    try:
        resposta = requests.get(
            f"{base_url}/clientes/{cliente_id}", timeout=3
        )
    except requests.Timeout as erro:
        raise ClienteIndisponivel(
            "Serviço de clientes temporariamente indisponível."
        ) from erro

    if resposta.status_code == 404:
        return None

    if resposta.status_code != 200:
        raise ClienteIndisponivel(
            "Serviço de clientes retornou uma falha."
        )

    return adaptar_cliente(resposta.json())
