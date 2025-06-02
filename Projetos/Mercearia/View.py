import Controller
import os.path

def criaArquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i,"w") as arq:
                arq.write("")

criaArquivos("categoria.txt","clientes.txt","estoque.txt","fornecedores.txt","funcionarios.txt","vendas.txt")

if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar ( Categorias )\n"
                          "Digite 2 para acessar ( Estoque )\n"
                          "Digite 3 para acessar ( Fornecedor )\n"
                          "Digite 4 para acessar ( Cliente )\n"
                          "Digite 5 para acessar ( Funcionario )\n"
                          "Digite 6 para acessar ( Vendas )\n"
                          "Digite 7 para ver os produtos mais vendidos\n"
                          "Digite 8 para sair"))
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostar as categorias cadastradas\n"
                                    "Digite 5 para sair"))
                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar: \n")
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que deseja remover: \n")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input("Digite a categoria que deseja alterar: \n")
                    novaCategoria = input("Digite a categoria para qual deseja alterar: \n")
                    cat.alterarCategoria(categoria,novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break

        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para ver o estoque\n"
                                    "Digite 5 para sair"))
                if decidir == 1:
                    nomeProduto = input("Digite o nome do produto que deseja cadastrar: ")
                    precoProduto = input("Digite o preço do produto que deseja cadastrar: ")
                    categoriaProduto = input("Digite a categoria do produto que deseja cadastrar: ")
                    quantidadeProduto = input("Digite a quantidade do produto que deseja cadastrar: ")
                    cat.cadastrarProduto(nomeProduto,precoProduto,categoriaProduto,quantidadeProduto)
                elif decidir == 2:
                    produto = input("Digite o produto que deseja remover: ")
                    cat.removerProduto(produto)
                elif decidir == 3:
                    produto = input("Digite o produto que deseja alterar: \n")
                    novoProduto = input("Digite o produto para qual deseja alterar: \n")
                    precoProduto = input("Digite o preço do produto que deseja cadastrar: ")
                    categoriaProduto = input("Digite a categoria do produto que deseja cadastrar: ")
                    quantidadeProduto = input("Digite a quantidade do produto que deseja cadastrar: ")
                    cat.alterarCategoria(produto,novoProduto,precoProduto,categoriaProduto,quantidadeProduto)
                elif decidir == 4:
                    cat.mostrarEstoque()
                else:
                    break

        elif local == 3:
            cat = Controller.ControllerFornecedor()

            