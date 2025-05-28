# Receba um número e mostra a tabuada completa dele usando o laço for

numero = int(input("Digite o número desejado: "))

for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")