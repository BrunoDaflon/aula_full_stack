class RepositorioChamados:
    def __init__(self):
        self.registros = []

    def salvar(self, chamado):
        chamado_persistido = {"id": len(self.registros) + 1, **chamado}
        self.registros.append(chamado_persistido)
        return chamado_persistido

    def listar(self):
        return self.registros


class ServicoChamados:
    prioridades_aceitas = {"baixa", "media", "alta"}

    def __init__(self, repositorio):
        self.repositorio = repositorio

    def criar(self, titulo, descricao, prioridade):
        if not titulo.strip() or not descricao.strip():
            raise ValueError("Título e descrição são obrigatórios.")

        if prioridade not in self.prioridades_aceitas:
            raise ValueError("Prioridade inválida.")

        chamado = {
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": "aberto"
        }
        return self.repositorio.salvar(chamado)


repositorio = RepositorioChamados()
servico = ServicoChamados(repositorio)

criado = servico.criar("Acesso bloqueado", "Não consigo acessar o painel.", "alta")
print(criado)
print(repositorio.listar())
