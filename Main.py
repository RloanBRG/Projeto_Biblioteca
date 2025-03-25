from Livros import Livro_Objeto # Importação de funções de outro arquivo
from Usuarios import Usuario_Objeto  
import json

def carregar_json(): # Carregar informações do arquivo biblioteca.json
        try:
            with open("biblioteca.json", "r") as f:
                data = json.load(f)
                for livros in data["Livros"]:
                    print(livros)
        except FileNotFoundError:
            print("Erro de codigo")


def menu():
    while True: #Menu de opções principal
        print("")
        print("----Menu Principal----")
        print("")
        print("1: Cadastro de livros")
        print("2: Cadastro de Usarios (em produção)")
        print("3: Emprestimo (em produção)")
        print("4: Devolução (em produção)")
        print("5: Listar livros (em produção)")
        print("0: Sair")


        option = int(input("Select a option: ")) # Selecionador de opção

        if option == 1: #Criação de um livro
            titulo = input("Digite o Titulo: ")
  
            while True: #Loop de verificação se input é um digito
                ano = input("Qual o ano de lançamento? (somente numeros): ")
                if ano.isdigit():
                    break
                else: # Caso não
                    print("Valor inserido não é um numero")

            genero = input("Qual o genero do livro? (Ex: ação, misterio, romance...): ")
            autor = input("Qual o nome do autor do livro?: ")
            disponivel = True

            novo_livro = Livro_Objeto(id, titulo, ano, genero, autor, disponivel)
            novo_livro.exibir_dados()
            novo_livro.salvar_json()
            print("codigo roda, porem falta implementação de funções de conexão com arquivo json")

        elif option == 2:
            print("função não codificada")

        elif option == 314: # Codigo debug se função carregar json funciona
            carregar_json()

        elif option == 0: # Fechamento do programa
            print("Adeus")
            break

        else: # Caso valor inserido em "option" seja diferente dos casos
            print("Tente novamente")


menu()
