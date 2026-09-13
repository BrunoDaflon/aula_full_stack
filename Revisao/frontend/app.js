const apiUrl = "http://127.0.0.1:8000/chamados";
const lista = document.querySelector("#lista");
const mensagem = document.querySelector("#mensagem");
const formulario = document.querySelector("#formulario");

function mostrarMensagem(texto) {
  mensagem.textContent = texto;
}

function renderizarLista(chamados) {
  lista.innerHTML = "";

  if (chamados.length === 0) {
    lista.innerHTML = "<li>Nenhum chamado cadastrado.</li>";
    return;
  }

  chamados.forEach((chamado) => {
    const item = document.createElement("li");
    item.textContent = `${chamado.titulo} — ${chamado.prioridade}`;
    lista.appendChild(item);
  });
}

async function carregarChamados() {
  mostrarMensagem("Carregando chamados...");

  try {
    const resposta = await fetch(apiUrl);
    if (!resposta.ok) {
      throw new Error("Falha ao consultar chamados.");
    }

    const chamados = await resposta.json();
    renderizarLista(chamados);
    mostrarMensagem("");
  } catch (erro) {
    mostrarMensagem("Não foi possível carregar os chamados.");
  }
}

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();

  const dados = {
    titulo: document.querySelector("#titulo").value,
    descricao: document.querySelector("#descricao").value,
    prioridade: document.querySelector("#prioridade").value
  };

  mostrarMensagem("Enviando chamado...");

  try {
    const resposta = await fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados)
    });

    if (!resposta.ok) {
      const erro = await resposta.json();
      throw new Error(erro.detail || "Dados inválidos.");
    }

    formulario.reset();
    mostrarMensagem("Chamado cadastrado com sucesso.");
    await carregarChamados();
  } catch (erro) {
    mostrarMensagem(erro.message || "Não foi possível cadastrar o chamado.");
  }
});

carregarChamados();
