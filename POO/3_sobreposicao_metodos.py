'''class Pessoas:

    def andar(self):
        print("Estou andando")

    def falar(self):
        print("Estou falando")

class Cliente(Pessoas):

    def comprar(self):
        print("Estou comprando")
    
    def falar(self): # Mesmo com o nome igual, a ordem de execução é sempre da classe filha (Cliente) pra classe pai (Pessoas)
        print("Estou gritando")
    
    def andar(self):
        super().andar() # Vai referenciar a classe pai (Pessoas) e executa essa linha
        print("Estou correndo") # Executa essa linha logo após


c1 = Cliente()



class Pessoas:

    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoas):

    def __init__(self, id_cliente,nome,cpf):
        super().__init__(nome,cpf)
        self.id_cliente = id_cliente

class Vendedor(Pessoas):

    def __init__(self, id_vendedor,nome, cpf):
        super().__init__(nome, cpf)
        self.id_vendedor = id_vendedor


c1 = Cliente(2, "Caio Sampaio", "43124213421")

print(c1.id_cliente)
print(c1.nome)

v1 = Vendedor("1", "Marcos Pedro", "9423109421")
print(v1.id_vendedor)
print(v1.nome)

'''

class Animal:
    def andar(self):
        print("Estou andando como um animal")

    def correr(self):
        print("Estou correndo")

    def pular(self):
        print("Estou pulando")

class Felino(Animal):
    def felino(self):
        print("Eu sou um felino")

class Gato(Felino):
    def miar(self):
        print("Estou andando como um gato")

class Cachorro(Animal):
    def latir(self):
        print("Estou latindo")

g1 = Gato()

g1.andar() # Vai funcionar esse metodo de animal pois Gato herda Felino e esse Felino está herdando Animal