numeros = [int(input(f"Digite o número: ")) for i in range(0,10)]

soma = 0

for num in numeros:
    soma += num
    
print(f"Soma dos valores{soma}")