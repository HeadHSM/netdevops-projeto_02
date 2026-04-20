from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

db_dispositivos = create_engine("sqlite:///dispositivos.db")
SessionDispositivos = sessionmaker(bind=db_dispositivos)
session_dispositivos = SessionDispositivos()

db_servidores = create_engine("sqlite:///servidores.db")
SessionServidores = sessionmaker(bind=db_servidores)
session_servidores = SessionServidores()

BaseDispositivos = declarative_base()
BaseServidores = declarative_base()

class Dispositivo(BaseDispositivos):
    __tablename__ = "dispositivos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    grupo = Column(String)
    user_root = Column(String)
    ip_addr = Column(String)
    ssh_key = Column(String)
    ativo = Column(Boolean, default=True)

class Servidor(BaseServidores):
    __tablename__ = "servidores"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    grupo = Column(String)
    user_root = Column(String)
    ip_addr = Column(String)
    ssh_key = Column(String)
    ativo = Column(Boolean, default=True)

BaseDispositivos.metadata.create_all(bind=db_dispositivos)
BaseServidores.metadata.create_all(bind=db_servidores)