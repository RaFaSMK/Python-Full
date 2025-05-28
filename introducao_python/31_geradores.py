from pympler.asizeof import asizesof

def dobro(lista):
    for i in lista:
        # O yield gera um valor e pausa a função, lembrando onde parou.
        # Ele só armazena o estado atual e o último valor gerado.
        yield i*2 

def dobro2(lista):
    lista_2 = []
    for i in lista:
        lista_2.append(i)
    # O return cria uma lista completa com todos os valores,
    # armazenando tudo na memória de uma vez.
    return lista_2

x = dobro(range(0,100)) # Cria um gerador. Nenhum valor é processado ainda e ele só gera valores sob demanda, consumindo pouca memória.
y = dobro2(range(0,100)) # Executa a função inteira e guarda todos os valores em uma lista e isso consome mais memória, pois todos os itens já existem.


# Mostra o uso de memória de cada estrutura
print(asizesof(x))
print(asizesof(y))