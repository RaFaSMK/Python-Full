# Escrever um programa que o usuário digite duas notas e ele mostre a média das duas notas

nota1 = float(input("Digite a primeira nota: ")) # O input sempre pega o dado como string, usei o float para converter
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(media)