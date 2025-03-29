class Usuario_Objeto: # Cria Usuarios
    def __init__ (self, name, idade, email, tipo):
        self.name = name
        self.idade = idade
        self.email = email
        self.tipo = tipo

    def atualizar_usuario():
        ...

    def deletar_usuario():
        ...

    def adicionar_usuario():
        ...

    def verificar_idade_permição(self):
        if self.idade > 18:
            print("Acesso a livros de maior idade")
            
        elif self.idade >= 16:
            print("Acesso limitado a livros violentos")

        else:
            print("Não tem acesso a livros de maior idade")
