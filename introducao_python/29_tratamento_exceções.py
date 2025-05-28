n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

try: # Ele tenta executar esse código se funcionar entra nele e se não funcionar entra no except
    print(n1/n2)
except: # Caso o try não funcione e dê algum erro, ele entra nesse except
    print("Não consegui")
finally: # Esse sempre vai ser executado
    print("Finalizado")

try:
    x = int(input("Digite um número: "))
    print(5/x)
except ValueError: # Se a operação retornar um erro de valor, que vem digitando algo que não é um numero inteiro
    print("Digite um número inteiro!")
except ZeroDivisionError: # Se a operação retornar um erro de divisão por 0, que vem com ele tentando dividir algo por 0
    print("Não digite 0!")


try:
    x = int(input("Digite um número: "))
    print(5/x)
except Exception as e: # Capturando qual excessão que está acontecendo e armazenando na variável e
    print(e)