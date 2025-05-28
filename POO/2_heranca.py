class Pessoa():

    def andar(self):
        print("Estou andando")

    def falar(self):
        print("Estou falando")

class Cliente(Pessoa): # Ja tem os metodos andar e falar, pois Cliente é uma Pessoa
    
    def comprar(self):
        print("Estou comprando")

class Vendedor(Pessoa):

    def vender(self):
        print("Estou vendendo")
