# Defina um usuário e senha e depois verifique se o login de usuário é válido

usr = "rafael"
senha = 123

while True:
    usr_input = input("Digite o usuário: ")
    senha_input = int(input("Digite a senha: "))
    if usr == usr_input and senha == senha_input:
        print("Usuário e senha correta!")
        break
    print("Usuário e senha incorreta! Digite novamente")