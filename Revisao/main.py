from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

chamados = []
prioridades_aceitas = {"baixa", "media", "alta"}


class ChamadoEntrada(BaseModel):
    titulo: str
    descricao: str
    prioridade: str


@app.get("/chamados")
def listar_chamados():
    return chamados


@app.post("/chamados", status_code=status.HTTP_201_CREATED)
def criar_chamado(dados: ChamadoEntrada):
    if not dados.titulo.strip() or not dados.descricao.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Título e descrição são obrigatórios."
        )

    if dados.prioridade not in prioridades_aceitas:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A prioridade deve ser baixa, media ou alta."
        )

    chamado = {
        "id": len(chamados) + 1,
        "titulo": dados.titulo,
        "descricao": dados.descricao,
        "prioridade": dados.prioridade,
        "status": "aberto"
    }
    chamados.append(chamado)
    return chamado
