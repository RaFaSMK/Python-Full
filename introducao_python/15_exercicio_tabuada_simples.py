# Receba um número do usuário e mostre a tabuada desse número

n = int(input("Numero desejado: "))

count = 1

while count <= 10:
    print(f"{n} x {count} = {n*count}")
    count+=1