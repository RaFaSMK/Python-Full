#Receba F para feminino e M para masculino e exiba o sexo da pessoa.

sexo = input("Digite F para sexo feminino e M para masculino: ")

if sexo == "F" or sexo == "f":
    print(f"Seu sexo é: Feminino")
elif sexo == "M" or sexo == "m":
    print(f"Seu sexo é: Masculino")
else:
    print("Sexo inválido")