import bcrypt
from sqlalchemy import create_engine # Cria o Banco de Dados
from sqlalchemy import Column, Integer, String, Boolean # Importando bibliotecas para o DB
from sqlalchemy.orm import sessionmaker, declarative_base # sessionmaker cria as sessões do DB e declarative_base cria as tabelas

db = create_engine("sqlite:///usuarios.db")
Session = sessionmaker(bind=db) # Cria a sessão para o Banco de Dados
session = Session() # Atribui o session com o 'S' minusculo

Base = declarative_base() # Atribui o valor da função declarative_base a Base

class Usuario(Base): # Tabela usuarios
    __tablename__ = "usuarios" # Nome da tabela obrigatório
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    cargo = Column(String)
    senha = Column(String)
    ativo = Column(Boolean, default=True)


Base.metadata.create_all(bind=db) # Cria o Banco de Dados

