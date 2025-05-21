from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Filme(BaseModel):
    titulo: str
    ano: int
    genero: str
 
filmes = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/filmes")
def adicionar_filme(filme: Filme):
    filmes.append(filme)
    return {"mensagem": "Filme adicionado com sucesso"}


@app.get("/filmes")
def listar_filmes():
    return filmes

@app.get("/filmes/{nome}")
def ver_filme(nome: str):
    for filme in filmes:
        if filme.titulo.lower() == nome.lower():
            return filme
    raise HTTPException(status_code=404, detail="Filme não encontrado")