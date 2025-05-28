#  Mostra a tabuada completa de todos os números entre 1 a 10.

for i in range (1,11):
    print(f"====================[TABUADA {i}]====================")
    for j in range (1,11):
        print(f"{i} x {j} = {i*j}")