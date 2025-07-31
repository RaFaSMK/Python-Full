from fastapi import FastAPI

app = FastAPI()

@app.get('/') #Endpoint padrao
def root():
    x = 10
    for i in range(10):
        x += 1
    return {'mensagem': 'home', 'valor' : x}

@app.get('/cadastro') #Endpoint cadastro
def cadastro():
    return {'mensagem': 'cadastro'}

@app.get('/login')
def login():
    return {'mensagem': 'login'}