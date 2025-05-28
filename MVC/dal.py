from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa): # Aqui ta indicando que o parametro pessoa, tem que ser uma instancia da classe Pessoa
        with open("pessoas.txt", "w") as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)

    @classmethod
    def ler(cls):
        nome = "Caio" # Exemplo do que leriamos do banco de dados
        idade = 20 # Exemplo do que leriamos do banco de dados
        cpf = 10321321321 # Exemplo do que leriamos do banco de dados
        return Pessoa(nome,idade,cpf) # Aqui vai retornar direto e não vai guardar em uma variavel