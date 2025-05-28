x = lambda: print("Olá") # Sempre retorna algo, mesmo sem usar a palavra reservada return e não precisa ser declarada
x()

y = lambda nome, idade: print(f"Nome = {nome} \nIdade = {idade}") # Recebe parâmetros
y("Rafael", "19")

z = lambda *idade: print(f"Idade: {idade}") # Pode usar um args e um kwargs
z("19","21","22","29","59")

def teste():
    return lambda *idade: print(idade)

x = teste()

x("Caio","Marcos")