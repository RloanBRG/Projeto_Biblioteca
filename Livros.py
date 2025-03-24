class book_overview: # Cria um objeto Livro
    def __init__ (self, id, titulo, ano, genero, autor, disponivel):
        self.id = id
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.autor = autor
        self.disponivel = disponivel

    def exibir_dados(self):
        return (f"titulo: {self.titulo}, ano: {self.ano}, genero: {self.genero}, autor: {self.autor}")
    
    def salvar_json(self):
        print("Função não construida")


    def carregar_json(self):
        print("Função não construida")