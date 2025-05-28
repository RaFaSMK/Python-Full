class Pessoas:
    possui_olho = True # Todas as instancias vao ter esse atributo, pois é um atributo de classe
    possui_boca = True
    raca = "Ser humano"

    def __init__(self,nome,idade): # É chamado sempre que instanciar uma classe
        self.nome = nome
        self.idade = idade
        nome_pessoa = nome # Não funciona, pois ele tem que saber qual intancia que é, usando o self

    def retorna_nome(self): # Esses 3 def, são atributos de instancia
        return self.nome
    
    def logar_sistema(self):
        print(f"{self.retorna_nome()} Está logando no sistema") # Sem o self ele não vai encontrar a instancia para poder chamar o método

    @classmethod # Metodo de classe
    def andar(cls): # cls recebe o estado da classe, tudo oq ela tem
        cls.pernas = 2 # Quando esse metódo é chamado cria um atributo de classe tipo o possui_olho
        return None
    
    @staticmethod
    def e_adulto(idade): # Metodo utilitario, não acessa os atributos da classe
        if idade > 18:
            return True
        return False

p1 = Pessoas("Caio Sampaio", 21) # Isso é uma instância
p2 = Pessoas("Marcos Sampaio", 42)

p1.possui_boca = False
print(p1.possui_boca)
Pessoas.possui_olho = False
print(p2.possui_olho)

Pessoas.andar(10)

print(Pessoas.e_adulto(21))