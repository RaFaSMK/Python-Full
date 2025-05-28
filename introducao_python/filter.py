x = [12,13,14,15,16,17,18,19,20,21,22,23,24,25]

x = list(filter(lambda x: x < 18 or x % 2 == 0, x)) # Recebe 2 parâmetros, uma função e a lista que quer aplicar o filter
print(x)

y = [{"nome": "Caio", "idade": 20},{"nome": "Marcos", "idade": 50}]

y = list(filter(lambda y: y["idade"] <= 20, y)) # Recebe 2 parâmetros, uma função e a lista que quer aplicar o filter
print(y)