def soma(n1,n2):
    if n1 < 0 or n2 < 0: 
        raise ValueError("n1 e n2 não podem ser negativos") # raise chama uma excessão que para o programa e da uma descrição para ela
    return n1+n2

print(soma(2,0))

x = -2
assert x > 0, "Deu merda" # Força que o x seja maior que 0, se não for ele da uma excessão que para o programa e coloca a descrição
print(x)