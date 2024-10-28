from services.usuario_service import UsuarioService
from repositores.usuario_repository import UsuarioRepository
from config.database import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    print("\nadicionando usuário:")
    nome = input("digite seu nome: ")
    email = input("digite seu e-mail: ")
    senha = input("digite sua senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    print("\nlistando usuários cadastrados")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - E-Mail: {usuario.email} - Senha: {usuario.senha}")
    
if __name__ == "__main__":
    os.system("cls || clear")
    main()