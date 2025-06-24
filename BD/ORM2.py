from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from ORM import Pessoa

def RetornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "aulapythonfull"
    PORT = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}" 

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session =  RetornaSession()

x = Pessoa(nome="caio",
           usuario="caio",
           senha="1234")

y = Pessoa(usuario="marcos", # Aqui o nome no BD vai ser null
           senha="1234") 

"""
session.add(x)
session.add(y)
"""
# OU
session.add_all([x,y])

session.rollback() #Apaga o add da session e deixa vazia, nesse caso como ela está em cima do commit, o commit não vai fazer nada
session.commit() #Persistir no banco de dados

"""
Python -> Session -> Engine (Banco de dados)
"""

x = session.query(Pessoa).all()
y = session.query(Pessoa).filter(Pessoa.nome == "caio") # Vai selecionar todos que se chamam "caio"

z = session.query(Pessoa).filter(Pessoa.nome == "caio").filter(Pessoa.usuario == "marcos") # Vai selecionar todos que se chamam "caio" e todos que tem o usuário de "marcos"
#OU
z = session.query(Pessoa).filter_by(nome="caio",usuario="marcos") # Vai selecionar todos que se chamam "caio" e todos que tem o usuário de "marcos"

j = session.query(Pessoa).filter(or_(Pessoa.nome == "caio", Pessoa.usuario == "marcos")).all() # O Pessoa no paramêtro é a tabela, o .all é para retornar uma lista e o or é o OU

print(x[0].id) # Vai selecionar a primeira linha do BC por causa do [0] e a coluna que você digitar após o .

for i in x:
    print(i.id) # Vai passar por todas as linhas e exibir o valor dos IDs

for i in y:
    print(i.id) # Vai exibir os IDs de todos os "caio"

for i in j:
    print(i)


x = session.query(Pessoa).filter(Pessoa.nome == "caio").all()

x[0].senha = "5678"
x[0].nome += "melo"

x = session.query(Pessoa).filter(Pessoa.nome == "caio").delete() # Para deletar a linha
#OU
x = session.query(Pessoa).filter(Pessoa.nome == "caio").one()
session.delete(x)


session.commit()