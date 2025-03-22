class book_overview: # Cria um objeto Livro
    def __init__ (self, id, titulo, ano, genero, autor, disponivel):
        self.id = int(id)
        self.titulo = titulo
        self.ano = int(ano)
        self.genero = genero
        self.autor = autor
        self.disponivel = bool(disponivel)