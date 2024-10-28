from services.usuario_service import UsuarioService
from repositores.usuario_repository import UsuarioRepository
from config.database import Session
import os


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        print("código\t|\tdescriação")
        print("1\t|\tcriar usuário")
        print("2\t|\tpesquisar um usuário")
        print("3\t|\tatualizar dados de um usuário")
        print("4\t|\texcluir usuário")
        print("5\t|\tlistar todos")
        print("0\t|\tsair")

        resposta = int(input("informe o código desejado:\n"))

        match(resposta):
            case 1:
                print("\nadicionando usuário:")
                nome = input("digite seu nome: ")
                email = input("digite seu e-mail: ")
                senha = input("digite sua senha: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)
            
            case 2:


    print("\nlistando usuários cadastrados")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(
            f"Nome: {usuario.nome} - E-Mail: {usuario.email} - Senha: {usuario.senha}"
        )


if __name__ == "__main__":
    os.system("cls || clear")
    main()
