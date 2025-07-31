from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: Optional[str] # Quer dizer que o nome e opcional e pode ser que nao seja usado toda vez
    senha: str

lista = [
    Usuario(id = 1 , nome="Rafael", senha="minhasenha1"),
    Usuario(id = 2, nome="Lucas", senha="minhasenha2"),
    Usuario(id = 3, nome="Jose", senha="minhasenha3")
]

@app.post('/usuario')
def main(usuario: Usuario):
    lista.append(usuario)
    return "Usario cadastrado"

@app.get('/usuarioListar')
def main():
    return lista