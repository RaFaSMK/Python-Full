from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

usuarios = [(1, "rafael", "minhasenha1"),(2, "lucas", "minhasenha2")]

@app.get('/usuario/{id}')
def main(id: int): # Esse id do parametro está como Int, se tivesse sem indicacao seria string
    for u in usuarios:
        if u[0] == id:
            return u
    return "Usuário com esse ID não existe"

@app.post('/usuario')
def main(nome):
    for i in usuarios:
        if i[1] == nome:
            return i
    return "Não existe esse usuario"