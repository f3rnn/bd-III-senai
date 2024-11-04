from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = self._verificar_nome(nome)
        self.email = email
        self.senha = senha
    
    def _verificar_nome_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("o nome deve ser um texto")
        
    def _verificar_nome_vazio(self, valor):
        if not valor.strip():
            raise TypeError("o nome não pode estar vazio")
        
    def _verificar_nome(self, valor):
        try:
            self._verificar_nome_invalido(valor)
            self._verificar_nome_vazio(valor)
        except TypeError as e:
            print(f"erro: {e}")
        except Exception as e:
            print(f"erro inesperado: {e}")
        self.nome = valor
        return self.nome

Base.metadata.create_all(bind=db)