class Usuario_Objeto: # Cria Usuarios
<<<<<<< HEAD
    def __init__ (self, id: int, nome: str, idade: int, email: str, tipo: str):
        self.id = id
        self.nome = nome
=======
    def __init__ (self, name, idade, email, tipo):
        self.name = name
>>>>>>> a2877fe61eacd447534e3eddb950577193e86555
        self.idade = idade
        self.email = email
        self.tipo = tipo

<<<<<<< HEAD
    def para_dicionario(self): # Retorna o que seria uma lista de dados de um livro em um dicionario, tipo aceito em json para que o salvamento ocorra
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email,
            "tipo": self.tipo
            
        }
=======
    def atualizar_usuario():
        ...

    def deletar_usuario():
        ...

    def adicionar_usuario():
        ...
>>>>>>> a2877fe61eacd447534e3eddb950577193e86555

    def verificar_idade_permição(self):
        if self.idade > 18:
            print("Acesso a livros de maior idade")
            
        elif self.idade >= 16:
            print("Acesso limitado a livros violentos")

        else:
            print("Não tem acesso a livros de maior idade")
