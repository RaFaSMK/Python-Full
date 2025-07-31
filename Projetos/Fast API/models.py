from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone

USUARIO = 'root'
SENHA = ''
HOST = 'localhost'
BANCO = 'aulafastapi'
PORT = '3306'

CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))

class Tokens(Base): #Esse token serve para ficar logado por tanto tempo no site, para caso roubem acessem por pouco tempo, em vez da senha que não expira
    __tablename__ = "Tokens"
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('Pessoa.id')) # Para saber de quem é aquele token
    token = Column(String(100))
    data = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

Base.metadata.create_all(engine)