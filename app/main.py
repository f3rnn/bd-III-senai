from services.usuario_service import UsuarioService
from repositores.usuario_repository import UsuarioRepository
from config.database import Session
from models.usuario_model import Usuario
import os




def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    def listar_usuario():
        print("\nlistando usuários cadastrados")
        lista_usuarios = service.listar_todos_usuarios()
        for usuario in lista_usuarios:
            print(
                f"Nome: {usuario.nome} - E-Mail: {usuario.email} - Senha: {usuario.senha}")


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
                listar_usuario()
                email=input("informe o e-mail do usuário que deseja procurar: ")
                if repository.pesquisar_usuario_por_email(email=email):
                    print(f"{usuario.nome} - {usuario.email} - {usuario.senha}")
                else:
                    print("usuário não encontrado")
                
            case 3:
                listar_usuario()
                nome= input("confirme o nome do usuário que deseja atualizar")     
                email= input("confirme o email do usuário que deseja atualizar")     
                senha= input("confirme o nome do usuário que deseja atualizar")
                usuario = Usuario(nome=nome, email=email,senha=senha)

                novo_nome = input("confirme o novo nome")
                novo_email = input("confirme o novo email")
                novo_senha = input("confirme o novo senha")
                usuario = Usuario(nome=novo_nome, email=novo_email, senha=novo_senha)
                repository.salvar_usuario(usuario=Usuario)
            case 4:
                listar_usuario()
                nome= input("confirme o nome do usuário que deseja excluir")     
                email= input("confirme o email do usuário que deseja excluir")     
                senha= input("confirme o nome do usuário que deseja excluir")
                usuario = Usuario(nome=nome, email=email,senha=senha)

                repository.excluir_usuario(usuario=usuario)

            case 5:
                listar_usuario()
            
            case 6:
                break
            case _:
                print("código incorreto, tente novamente")


if __name__ == "__main__":
    os.system("cls || clear")
    main()
