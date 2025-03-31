<<<<<<< HEAD
=======
import json
>>>>>>> a2877fe61eacd447534e3eddb950577193e86555

class Livro_Objeto: # Cria um objeto Livro
    def __init__ (self, id: int, titulo: str, ano: int, genero: str, autor: str, disponivel: bool): # Contrutor do objeto livros
        self.id = id
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.autor = autor
        self.disponivel = disponivel

<<<<<<< HEAD
    def para_dicionario(self): # Retorna o que seria uma lista de dados de um livro em um dicionario, tipo aceito em json para que o salvamento ocorra
        return {
            "id": self.id,
            "titulo": self.titulo,
            "ano": self.ano,
            "genero": self.genero,
            "autor": self.autor,
            "disponivel": self.disponivel
        }

    def exibir_dados(self): # Função de retorno de informações
        print(f"Titulo: {self.titulo},\nAno: {self.ano},\nGenero: {self.genero},\nAutor: {self.autor}")
        
=======
    def exibir_dados(self): # Função de retorno de informações
        print(f"Titulo: {self.titulo},\nAno: {self.ano},\nGenero: {self.genero},\nAutor: {self.autor}")
    
    def salvar_json(self): # Em andamento
        print("Função não construida") 
>>>>>>> a2877fe61eacd447534e3eddb950577193e86555
