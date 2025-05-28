nomes = ['Caio','Marcos','Joao','Pedro']

nomes[0] = 'Caio Sampaio'

nomes.append('Jose') # Adiciona no final da lista
nomes.insert(pos,nome) # Insere o elemento na posição desejada, se tiver 5 elementos e digitar a posição 9, vai inserir na ultima
print(len(nomes)) # len é o lenght, conta quantos elementos tem dentro da lista
nomes.pop() # Remove o ultimo
nomes.pop(pos) # Remove na posição passada no parâmetro
nomes.remove(valor) # Remove o elemento desejado e somente um, caso tiver dois
nomes.index(elemento) # Retorna o valor do index do elemento no parâmetro, tem que usar o print nele pra funcionar print(nomes.index(elemento)), encontrou sai do loop igual o remove
print(nomes)

while True:
    nome = input("Digite -1 para sair do programa ou cadastre um nome: ")
    if nome == '-1':
        break
    pos = int(input('Qual posição deseja armazenar? '))
    nomes.insert(pos,nome) # Insere o elemento na posição desejada, se tiver 5 elementos e digitar a posição 9, vai inserir na ultima
print(nomes)

for i in enumerate(nomes): # Exibe a tupla inteira da lista
    print(i)

for i in enumerate(nomes):  # Exibe o elemento do indicie 0 da tupla
    print(i[0])

for i in enumerate(nomes):  # Exibe o elemento do indicie 1 da tupla
    print(i[1])

for i,j in enumerate(nomes): # O i vai ser o primeiro elemento da tupla e j vai ser o segundo elemento
    print(f"i = {i} e j = {j}")

idades = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # Matriz de idades

x = [1,2,3] # Endereço na memória: 0x220fa34d900
y = x # Endereço na memória: 0x220fa34d900
y[0] = 0

print(x) # [0,2,3]
print(y) # [0,2,3]
# Isso acontece porque o y não é uma cópia de x, e sim a mesma lista, que aponta para o mesmo endereço de memória
# Ou seja, se você mudar o y vai mudar o x na lista, pois ambos estão apontando para o mesmo endereço

x = [1,2,3] # Endereço na memória: 0x25f41ebd900
y = x.copy() # Endereço na memória: 0x25f41ebd180
y[0] = 0 

print(x) # [1,2,3]
print(y) # [0,2,3]
# Agora isso acontece porque não apontam para o mesmo endereço na memória e sim cria uma nova lista, logo, um novo endereço

print(id(x)) # Id retorna o endereço de memória onde aquela variavel está
print(hex(id(x))) # Retorna o valor de Id em hexadecimal 
print(hex(id(y))) 