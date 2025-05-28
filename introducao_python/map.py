x = [{"nome": "Caio", "idade": 20},{"nome": "Marcos", "idade": 40}]
x = list(map(lambda x: 10 if x["idade"] < 38 else(x), x))
print(x)

x = [{"nome": "Caio", "idade": 20},{"nome": "Marcos", "idade": 40}]
x = list(map(lambda x: {"nome": "Caio", "idade": "Menor do que 30 anos"} if x["idade"] < 38 else(x), x))
print(x)

x = [{"nome": "Caio", "idade": 20},{"nome": "Marcos", "idade": 40}]
x = list(map(lambda x: {"nome": x["nome"], "idade": "menor do que 30 anos"} if x["idade"] < 38 else(x), x))
print(x)