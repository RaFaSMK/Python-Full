x = [1,2,2,3,4,5]
x = set(x) # Definir a lista como conjunto, os conjuntos não possuem valores repetidos
y = {4,5,6,7,8,9,10} # Se colocar um repetido, ele vai ser desconsiderado

print(x.union(y)) # Printa a união e se estiver presente nos 2 conjuntos ele vai printar uma vez só
print(x.intersection(y)) # Printa a intersecção, os valores aparecem nos 2 conjuntos
print(x.difference(y)) # Printa a diferença do x menos o y, pegar tudo que tem no x e retirar o que estiver no y
print(x.symmetric_difference(y)) # Printa a união só que se estiver presente nos 2 conjuntos ele vai excluir