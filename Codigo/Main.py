from Codigo_json import carregar_json, verificar_caminho, coletar_dados_livro, coletar_dados_usuario


def menu():
    while True: #Menu de opções principal
        print("")
        print("----Menu Principal----")
        print("")
        print("1: Cadastro de livros")
        print("2: Cadastro de Usarios")
        print("3: Emprestimo (em produção)")
        print("4: Devolução (em produção)")
        print("5: Listar livros (em produção)")
        print("0: Sair")


        option = int(input("Select a option: ")) # Selecionador de opção

        if option == 1: #Criação de um livro
            coletar_dados_livro()

        elif option == 2:
            coletar_dados_usuario()

        elif option == 314: # Codigo debug se função carregar json funciona
            verificar_caminho()
            print("")
            carregar_json()

        elif option == 0: # Fechamento do programa
            print("Adeus")
            break

        else: # Caso valor inserido em "option" seja diferente dos casos
            print("Tente novamente")


menu()
