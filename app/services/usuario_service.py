from models.usuario_model import Usuario
from repositores.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository
    
    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return
            
            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")

        except TypeError as erro:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")
    
    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()
    
    def excluir_usuario(self):
        try:
            email = input("informe o email desse usuário: \n")
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if cadastrado:
                senha = input("confirme a senha do usuário: \n")

                if senha == cadastrado.senha:
                    self.repository.excluir_usuario(cadastrado)
                    print("usuário excluído com sucesso")
                print("senha inválida!")
                return
            print("usuário não encontrado!")
            return

        except TypeError as erro:
            print(f"erro ao excluir usuário: {erro}")
        except Exception as erro:
            print(f"erro inesperado: {erro}")
    
    def atualizar_usuario(self):
        try:
            email = input("informe o email do usuário: \n")
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if cadastrado:
                cadastrado.nome = input("digite seu nome: \n")
                cadastrado.email = input("digite seu email: \n")
                cadastrado.senha = input("digite sua senha: \n")
                print("usuário atualizado com sucesso!")
                self.repository.salvar_usuario(cadastrado)
            print("usuário não encontrado")
            return
        
        except TypeError as erro:
            print(f"erro ao atualizar usuário: {erro}")
        except Exception as erro:
            print(f"erro inesperado: {erro}")
        
    def pesquisar_usuario_unico(self):
        try:
            email = input("informe o email do usuário: \n")
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if cadastrado:
                print("usuário encontrado!")
                print(f"nome: {cadastrado.nome} - {cadastrado.email} - {cadastrado.senha}")
                return
            print("usuário não encontrado")
            return
        
        except TypeError as erro:
            print(f"erro ao procurar o usuário: {erro}")
        except Exception as erro:
            print(f"erro inesperado: {erro}")
