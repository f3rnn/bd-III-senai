from services.usuario_service import UsuarioService
from repositores.usuario_repository import UsuarioRepository
from config.database import Session

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
        print(f"nome: {usuario.nome} - e-mail: {usuario.email} - senha: {usuario.senha}")
    
if __name__ == "main":
    main()