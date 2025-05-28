x = [i for i in range(0,10)] # Usando list comprehension, paradigma de programação na forma funcional
# O primeiro i é o elemento para adicionar como se fosse um append
# Depois do primeiro i é a estrutura de repetição


y = []
for i in range(0,10):
    y.append(i) # É a mesma coisa da processo acima mas, paradigma de programação na forma procedural


z = [i*2 for i in x] # Nesse caso vai adicionar cada elemento da lista x multiplicado por 2

l = [input("Digite o nome: ") for i in range(0,3)] 
# Aqui vai inserir na lista o input do usuário

g = [ [j for j in range(0,3)] for i in range(0,3)] 
# Vai criar uma lista adicionando o j com, [j for j in range(0,3)], pois sempre executa o list comprehension mais interno, ficando [[0,1,2]]
# E depois vai criar uma matriz de 3 linhas com o, for i in range(0,3), ficando [[0,1,2],[0,1,2],[0,1,2]]
# Ficando [[0,1,2], [0,1,2], [0,1,2]]

f = [i for i in range(0,10) if i > 4]
# Vai criar uma lista inserindo o valor de i no range(0,10) SE i > 4, assim que se faz usando uma condicional