for i in range(0,5): # Será executado 5 vezes, mas não passará no 5, pois é como se fose 0 < 5, ou seja, quando for pro 5 ele para antes, no 4
    print(i)

for i in range(2,100, 2): 
    print(i)

for i in range(100 , 0, -2):
    print(i)

x = ["a",1,2,3,"x","z"]

for i in x:
    print(i)

frase = input("Digite seu nome: ")

for letra in frase:
    print(letra)

for i in range(0,3):
    for j in range(0,3):
        print(f"i = {i} j = {j}")