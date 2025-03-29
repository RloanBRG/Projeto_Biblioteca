import json

class Livro_Objeto: # Cria um objeto Livro
    def __init__ (self, id: int, titulo: str, ano: int, genero: str, autor: str, disponivel: bool): # Contrutor do objeto livros
        self.id = id
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.autor = autor
        self.disponivel = disponivel

    def exibir_dados(self): # Função de retorno de informações
        print(f"Titulo: {self.titulo},\nAno: {self.ano},\nGenero: {self.genero},\nAutor: {self.autor}")
    
    def salvar_json(self): # Em andamento
        print("Função não construida") 