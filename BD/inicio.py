import pymysql.cursors

con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
    db="aulapythonfull"
    #Se não passar nada no parametro port, ele usa a padrão 3306
)
def criaTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"create table {nomeTabela} (nome varchar(50))")
        print("Tabela criada")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

def excluirTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
        print("Tabela excluida")
    except Exception as e:
        print(f"Erro ao excluir tabela: {e}")

def inserirTabela(nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO teste values('{nome}')")
        print("Valor inserido com sucesso")
    except Exception as e:
        print(f"Erro ao inserir na tabela: {e}")

def selectTabela():
    try:
        with con.cursor() as cursor:
            cursor.execute(f"select * from teste")
            resultado = cursor.fetchall()
            for i in resultado:
                # print(len(resultado)) vai aparecer a quantidade de linhas
                # print(len(resultado[0])) vai aparecer a quantidade de colunas
                print(i) 
    except Exception as e:
        print(f"Erro ao excluir tabela: {e}")

def updateTabela():
    try:
        with con.cursor() as cursor:
            cursor.execute(f"UPDATE teste SET nome = 'Marco' WHERE nome = 'marco'")
        print("Tabela alterada")
    except Exception as e:
        print(f"Erro ao excluir tabela: {e}")

def deleteTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DELETE FROM teste WHERE nome = 'joao'") # Remove TODOS que tenham o mesmo nome
        print("Remoção efetuada com sucesso")
    except Exception as e:
        print(f"Erro ao excluir tabela: {e}")

con.close()