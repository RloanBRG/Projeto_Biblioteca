class Usuario_Objeto: # Cria Usuarios
    def __init__ (self, id: int, nome: str, idade: int, email: str, senha: str, tipo: str):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.senha = senha
        self.email = email
        self.tipo = tipo

    def para_dicionario(self): # Retorna o que seria uma lista de dados de um livro em um dicionario, tipo aceito em json para que o salvamento ocorra
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": int(self.idade),
            "email": self.email,
            "senha": self.senha,
            "tipo": str(self.tipo)
            
        }

    def verificar_idade_permição(self):
        if self.idade > 18:
            print("Acesso a livros de maior idade")
            
        elif self.idade >= 16:
            print("Acesso limitado a livros violentos")

        else:
            print("Não tem acesso a livros de maior idade")

    def autenticacao_email(self):
        ...
