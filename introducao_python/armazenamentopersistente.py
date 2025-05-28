arquivo = open("pessoas.txt", "w") # Apaga tudo que tem no arquivo e escreve oq passou no .write
arquivo = open("pessoas.txt", "a") # Adiciona o texto dentro do um arquivo
arquivo = open("pessoas.txt", "r") # Ler o arquivo

arquivo = open("pessoas.txt", "a")
while True:
    arquivo.write(input("Digite o nome da pessoa: ") + "\n" + input("Digite a idade: ")) 

arquivo = open("pessoas.txt", "r")
resultados = arquivo.read() # Vai ler todos os elementos como string
print(resultados)

resultados = arquivo.readlines() # Le cada linha do arquivo e cada uma vai ser uma posição de uma lista
x = []
for i in resultados:
    x.append(i.split())
print(x)
arquivo.close() # Para fechar o arquivo e não deixar brechas de segurança e bugs

with open('pessoas.txt',"r") as arq: # Gerenciador de contexto que abre e fecha o arquivo automaticamente
    x = arq.read()
    print(x)