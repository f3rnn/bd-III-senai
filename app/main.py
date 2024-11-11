from app.services.usuario_service import UsuarioService
from app.repositores.usuario_repository import UsuarioRepository
from app.config.database import Session
from app.models.usuario_model import Usuario
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    def listar_usuario():
        print("listando usuários cadastrados")
        lista_usuarios = service.listar_todos_usuarios()
        for usuario in lista_usuarios:
            print(
                f"Nome: {usuario.nome} - E-Mail: {usuario.email} - Senha: {usuario.senha}")


    while True:
        print("\ncódigo\t|\tdescriação")
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
                listar_usuario()
                print("\n pesquisando usuário")
                service.pesquisar_usuario_unico()
                
            case 3:
                listar_usuario()
                service.atualizar_usuario()
               
            case 4:
                listar_usuario()
                print("\nexcluindo usuário:")
                service.excluir_usuario()

            case 5:
                listar_usuario()
            
            case 0:
                break
            case _:
                print("código incorreto, tente novamente")


if __name__ == "__main__":
    os.system("cls || clear")
    main()
