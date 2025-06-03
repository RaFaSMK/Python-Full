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
                          "Digite 8 para sair\n"))
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"))
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
                                    "Digite 5 para sair\n"))
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
                    precoProduto = input("Digite o novo preço do produto que deseja alterar: ")
                    categoriaProduto = input("Digite a nova categoria do produto que deseja alterar: ")
                    quantidadeProduto = input("Digite a nova quantidade do produto que deseja alterar: ")
                    cat.alterarProduto(produto,novoProduto,precoProduto,categoriaProduto,quantidadeProduto)
                elif decidir == 4:
                    cat.mostrarEstoque()
                else:
                    break

        elif local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para ver a lista de fornecedores\n"
                                    "Digite 5 para sair\n"))
                if decidir == 1:
                    nomeFornecedor = input("Digite o nome do fornecedor que deseja cadastrar: ")
                    cnpjFornecedor = input("Digite o cnpj do fornecedor que deseja cadastrar: ")
                    telefoneFornecedor = input("Digite o telefone do fornecedor que deseja cadastrar: ")
                    categoriaFornecedor = input("Digite a categoria do fornecedor que deseja cadastrar: ")
                    cat.cadastrarFornecedor(nomeFornecedor, cnpjFornecedor, telefoneFornecedor, categoriaFornecedor)
                elif decidir == 2:
                    fornecedor = input("Digite o fornecedor que deseja remover: ")
                    cat.removerFornecedor(fornecedor)
                elif decidir == 3:
                    nomeFornecedor = input("Digite o nome do fornecedor que deseja alterar: ")
                    novoNomeFornecedor = input("Digite o nome do fornecedor para qual deseja alterar: ")
                    cnpjFornecedor = input("Digite o novo cnpj do fornecedor que deseja alterar: ")
                    telefoneFornecedor = input("Digite o novo telefone do fornecedor que deseja alterar: ")
                    categoriaFornecedor = input("Digite a nova categoria do fornecedor que deseja alterar: ")
                    cat.alterarFornecedor(nomeFornecedor, novoNomeFornecedor, cnpjFornecedor, telefoneFornecedor, categoriaFornecedor)
                elif decidir == 4:
                    cat.mostrarFornecedor()
                else:
                    break

        elif local == 4:
            cat = Controller.ControllerCliente()
            while True:
                decidir = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para ver a lista de clientes\n"
                                    "Digite 5 para sair\n"))
                if decidir == 1:
                    nomeCliente = input("Digite o nome do cliente que deseja cadastrar: ")
                    telefoneCliente = input("Digite o telefone do cliente que deseja cadastrar: ")
                    cpfCliente = input("Digite o CPF do cliente: ")
                    emailCliente = input("Digite o e-mail do cliente: ")
                    enderecoCliente = input("Digite o endereco do cliente que deseja cadastrar: ")
                    cat.cadastrarCliente(nomeCliente, telefoneCliente, cpfCliente, emailCliente, enderecoCliente)
                elif decidir == 2:
                    cliente = input("Digite o nome do cliente que deseja remover: ")
                    cat.removerCliente(cliente)
                elif decidir == 3:
                    nomeCliente = input("Digite o nome do cliente que deseja alterar: ")
                    novoNomeCliente = input("Digite nome do cliente para qual deseja alterar: ")
                    telefoneCliente = input("Digite o novo telefone do cliente que deseja alterar: ")
                    cpfCliente = input("Digite o novo CPF do cliente que deseje alterar: ")
                    emailCliente = input("Digite o novo e-mail do cliente que deseja alterar: ")
                    enderecoCliente = input("Digite o novo endereco do cliente que deseja alterar: ")
                    cat.alterarCliente(nomeCliente, novoNomeCliente,telefoneCliente, cpfCliente, emailCliente, enderecoCliente)
                elif decidir == 4:
                    cat.mostrarCliente()
                else:
                    break

        elif local == 5:
            cat = Controller.ControllerFuncionario()
            while True:
                decidir = int(input("Digite 1 para cadastrar um funcionário\n"
                                    "Digite 2 para remover um funcionário\n"
                                    "Digite 3 para alterar um funcionário\n"
                                    "Digite 4 para ver a lista de funcionários\n"
                                    "Digite 5 para sair\n"))
                if decidir == 1:
                    nomeFuncionario = input("Digite o nome do funcionário que deseja cadastrar: ")
                    cltFuncionario = input("Digite o número da clt do funcionário que deseja cadastrar: ")
                    telefoneFuncionario = input("Digite o telefone do funcionario que deseja cadastrar: ")
                    cpfFuncionario = input("Digite o CPF do funcionário que deseja cadastrar: ")
                    emailFuncionario = input("Digite o e-mail do funcionario que deseja cadastrar: ")
                    enderecoFuncionario = input("Digite o endereco do funcionario que deseja cadastrar: ")
                    cat.cadastrarFuncionario(cltFuncionario, nomeFuncionario,telefoneFuncionario, cpfFuncionario,emailFuncionario,enderecoFuncionario)
                elif decidir == 2:
                    funcionario = input("Digite o nome do funcionário que deseja remover: ")
                    cat.removerFuncionario(funcionario)
                elif decidir == 3:
                    nomeFuncionario = input("Digite o nome do funcionário que deseja alterar: ")
                    novoNomeFuncionario = input("Digite nome do funcionário para qual deseja alterar: ")
                    cltFuncionario = input("Digite o novo número da clt do funcionário: ")
                    telefoneFuncionario = input("Digite o novo telefone do funcionario: ")
                    cpfFuncionario = input("Digite o novo CPF do funcionário: ")
                    emailFuncionario = input("Digite o novo e-mail do funcionario: ")
                    enderecoFuncionario = input("Digite o novo endereco do funcionario: ")
                    cat.alterarFuncionario( nomeFuncionario, cltFuncionario, novoNomeFuncionario, telefoneFuncionario, cpfFuncionario, emailFuncionario, enderecoFuncionario)
                elif decidir == 4:
                    cat.mostrarFuncionario()
                else:
                    break

        elif local == 6:
            cat = Controller.ControllerVenda()
            while True:
                decidir = int(input("Digite 1 para registrar uma venda\n"
                                    "Digite 2 para mostrar as vendas por data\n"
                                    "Digite 3 para sair\n"))
                if decidir == 1:
                    produto = input("Digite o nome do produto vendido: ")
                    vendedor = input("Digite o nome do vendedor: ")
                    cliente = input("Digite o nome do cliente: ")
                    quantidade = input("Digite a quantidade vendida: ")
                    cat.cadastrarVenda(produto,vendedor, cliente,quantidade)
                elif decidir == 2:
                    dataInicio = input("Digite a data de inicio no formato dd/mm/yyyy: ")
                    dataFinal = input("Digite a data final no formato dd/mm/yyyy: ")
                    cat.mostrarVenda(dataInicio,dataFinal)
                else:
                    break

        elif local == 7:
            cat = Controller.ControllerVenda()
            cat.relatorioProdutos()

        else:
            print("Saindo do sistema...")
            break