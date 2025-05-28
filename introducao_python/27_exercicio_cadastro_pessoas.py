# Faça um programa que o usuário possa cadastrar n pessoas,
# armazenando seu nome, idade e altura

lista_nomes = []

while True:
    opcao = int(input("Digite 1 para cadastrar uma pessoa e 2 para sair do programa: "))
    if opcao == 2:
        break
    pessoa = {'nome': input("Digite o nome: "), 
              'idade': int(input("Digite a idade: ")), 
              'altura': int(input("Digite a altura: "))}
    
    lista_nomes.append(pessoa)

print(f"Lista: {lista_nomes}")