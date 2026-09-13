const cenario = "sucesso"; // altere para: sucesso, ausente ou indisponivel
const area = document.querySelector("#cliente");

const respostas = {
  sucesso: {
    status: 200,
    corpo: {
      nome_cliente: "Ana Souza",
      codigo_unidade: "SP-01",
      cliente_ativo: true
    }
  },
  ausente: { status: 404, corpo: null },
  indisponivel: { status: 503, corpo: null }
};

async function consultarCliente() {
  area.textContent = "Carregando dados da pessoa cliente...";
  const resposta = respostas[cenario];

  if (resposta.status === 404) {
    area.textContent = "A pessoa cliente não foi encontrada.";
    return;
  }

  if (resposta.status !== 200) {
    area.textContent =
      "Não foi possível consultar os dados da pessoa cliente neste momento.";
    return;
  }

  const cliente = resposta.corpo;
  area.textContent = `${cliente.nome_cliente} — unidade ${cliente.codigo_unidade}`;
}

consultarCliente();
