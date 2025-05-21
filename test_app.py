import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_adicionar_filme():

    novo_filme = {
        "titulo": "Alien",
        "ano": 1979,
        "genero": "Ficção científica"
    }

    response = client.post("/filmes", json=novo_filme)

    assert response.status_code == 200
    assert response.json() == {"mensagem": "Filme adicionado com sucesso"}

def test_listar_filmes():
    response = client.get("/filmes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_ver_filme():
    novo_filme = {
        "titulo": "Inception",
        "ano": 2010,
        "genero": "Ficção científica"
    }
    client.post("/filmes", json=novo_filme)

    response = client.get("/filmes/Inception")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Inception"
    assert response.json()["ano"] == 2010

def test_ver_filme_nao_existente():
    response = client.get("/filmes/Nonexistent")
    assert response.status_code == 404
    assert response.json() == {"detail": "Filme não encontrado"}
