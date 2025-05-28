import pickle # O pickle NÃO é uma criptografia os dados e sim seralizando
# Serialização de objetos, pegar algo que ta em memória e tornar persistente

x = [1,2,3,4]

string = pickle.dumps(x)
print(string)
print(pickle.loads(string))

