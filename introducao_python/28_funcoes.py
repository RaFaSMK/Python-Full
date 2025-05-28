def soma_numeros(n1,n2,*args): # Recebe o primeiro parêmetro (n1) e o segundo (n2) e o resto empacota dentro de args que é uma tupla
    print(f"n1 = {n1} n2 = {n2} args={args}")
soma_numeros(1,2,3,4,5,6,7,8)


def testes(**kwargs): # Empacota tudo dentro do kwargs que é um dicionário
    print(kwargs) # Printa o dicionário
    x = kwargs.get('teste4') # Tenta pegar o dicionário com a chave teste4, se conseguir atribui o valor ao x e se não conseguir atribui none
    if x: # No python se não comparar e deixar só a variável o py entende que tudo é verdadeiro exceto o False e o none
        print('Foi passado') 
    else:
        print('Não foi passado')
testes(teste1 = 1, teste2 = 2, teste3 = 3)

def soma_valores(n1,n2):
    soma = n1+n2
    return soma, n1, n2 # Compacta a soma para dentro de uma tupla
    print('TO AQUI') # O código após o return não será executado

soma, n1, n2= soma_valores(1,2)

print(soma) # Printa o 3
print(n1) # Printa o 1
print(n2) # Printa o 2


def teste(t1,t2):
    soma = t1+t2
    if soma > 5:
        return soma
    print("To aqui")

print(teste(5,2))
print(teste(1,1))