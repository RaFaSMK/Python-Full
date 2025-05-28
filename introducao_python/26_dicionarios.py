pessoa = {'nome': 'Caio Sampaio', 'idade': 21, 'cep': '231321321'} # Dicionário simples
pessoa['nome'] = 'Marcos' # Acessa o dicionário e a chave 'nome' e atribui 'Marcos

print(pessoa) # Printa o dicionário
print(pessoa['nome']) # Printa 'Marcos' que é o nome que está atribuido na chave 'nome'

pessoas = [{'nome': 'Caio', 'idade': 21, 'altura': 173}, # Três dicionários dentro de uma lista
           {'nome': 'Marcos', 'idade': 21, 'altura': 173},
           {'nome': 'Pedro', 'idade': 21, 'altura': 173}]
for pessoa in pessoas: # Para cada elemento (dicionário) dentro da lista pessoas
    print(pessoa) # Printa cada dicionário por repetição
    print(pessoa['nome']) # Printa cada nome dos dicionários por repetição

# Atualizar dicionário
pessoa = {'nome': 'Caio', 'idade': 21, 'altura': 173}
pessoa['cep'] = '14407290' # Adiciona no dicionário a chave cep e o valor
pessoa.update({'cep': '14407290', 'rua': 'Minha rua'}) # Atualiza o dicionário, inserindo esses elementos
print(pessoa)

# Iterar sobre o dicionário
print(pessoa.values()) # Retorna os valores daquele dicionário, sem as chaves
print(pessoa.keys()) # Retorna as chanves daquele dicionário, sem os valores
print(pessoa.items()) # Retorna uma lista com cada valor e dentro dela tem uma tupla, com a chave e o valor

for i in pessoa:
    print(i) # Printa apenas a chave

for i, j in pessoa.items():
    print(f"i = {i} j = {j}") # Printa a chave e o valor