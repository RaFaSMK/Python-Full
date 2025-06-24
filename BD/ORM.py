from sqlalchemy import create_engine, Column, Integer, String, ForeignKey #create_engine, cria a conexão com o BD
from sqlalchemy.ext.declarative import declarative_base #declarative_base: Cria uma classe base para os modelos ORM (permite mapear classes Python para tabelas no banco de dados).
from sqlalchemy.orm import sessionmaker #sessionmaker: Cria uma fábrica de sessões para interagir com o banco (fazer insert, select, update, etc).

USUARIO = "root" # Letras maiúsculas para declaração de constantes
SENHA = ""
HOST = "localhost"
BANCO = "aulapythonfull"
PORT = "3306"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}" #Constrói a URL de conexão no formato esperado pelo SQLAlchemy para MySQL com o driver pymysql.

engine = create_engine(CONN, echo=True) #Cria o engine, que é a interface principal com o banco. 
                                        #echo True mostra os logs e oque está acontecendo, False mostra as mais importantes

Session = sessionmaker(bind=engine) #sessionmaker(bind=engine): liga a sessão ao banco definido no engine.
session = Session() #session = Session(): cria uma sessão ativa (uma "conexão" com o banco para fazer operações).

Base = declarative_base()#Cria a classe base a partir da qual todos os modelos (classes-tabela) devem herdar.
                         #Permite que o SQLAlchemy saiba como mapear objetos Python em tabelas do banco.

class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))

class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer,primary_key=True)
    categoria = Column(String(50))

class Produto(Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key=True)
    produto = Column(String(50))
    idCategoria = Column(Integer, ForeignKey('categoria.id'))

Base.metadata.create_all(engine) #Cria todas as tabelas definidas que ainda não existem no banco.
                                 #Base.metadata guarda o "modelo" das tabelas.
                                 #create_all(engine) envia os comandos CREATE TABLE para o banco.