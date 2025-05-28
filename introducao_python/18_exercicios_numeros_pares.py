# Receba o número e mostre todos os números pares de 0 até o número digitado

numero = int(input("Número desejado: "))

num = 1
while num <= numero:
    if num % 2 == 0:
        print(num)
    num+=1