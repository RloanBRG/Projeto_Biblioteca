from Livros import book_overview 
from Usuarios import user_type 

def menu():
    while True:
        print("")
        print("----Menu Principal----")
        print("")
        print("1: Cadastro de livros")
        print("2: Cadastro de Usarios")
        print("3: ...")
        print("4: ...")
        print("0: Sair")


        option = int(input("Select a option: "))

        if option == 1:
            titulo = input("Digite o Titulo: ")

            while True:
                ano = input("Qual o ano de lançamento? (somente numeros): ")
                if ano.isdigit():
                    break
                else:
                    print("Valor inserido não é um numero")

            genero = input("Qual o genero do livro? (Ex: ação, misterio, romance...): ")
            autor = input("Qual o nome do autor do livro?: ")
            disponivel = True

            novo_livro = book_overview(id, titulo, ano, genero, autor, disponivel)
            novo_livro.exibir_dados()
            novo_livro.salvar_json()
        elif option == 1:
            print("função nao codificada")

        elif option == 0:
            print("Adeus")
            break
        else:
            print("Tente novamente")
menu()