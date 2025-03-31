<<<<<<< HEAD
from Codigo_json import carregar_json, verificar_caminho, coletar_dados_livro, coletar_dados_usuario
=======
from Livros import Livro_Objeto # Importação de funções de outro arquivo
from Usuarios import Usuario_Objeto

import json # Leitura de arquivo json
import os #Localização do arquivo json

pasta_projeto = os.path.dirname(os.path.abspath(__file__)) # Verica onde o arquivo esta localizado no computador
caminho_json = os.path.join(pasta_projeto, "biblioteca.json") # Verica se existe um biblioteca para ser adionado no diretorio

def vericar_caminho():
    print(f"A pasta é {pasta_projeto}")
    print(f"o caminho do json é {caminho_json}")
    print("")

def carregar_json(): # Carregar informações do arquivo biblioteca.json
        try:
            with open(caminho_json, "r", encoding="utf-8") as f:
                data = json.load(f)
                for livros in data["livros"]:
                    print(livros)
                for usuario in data["usuarios"]:
                    print(usuario)

                return data
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado")
        except json.JSONDecodeError:
            print("Erro: não foi possivel decodificar o arquvo json")
>>>>>>> a2877fe61eacd447534e3eddb950577193e86555


def menu():
    while True: #Menu de opções principal
        print("")
        print("----Menu Principal----")
        print("")
        print("1: Cadastro de livros")
<<<<<<< HEAD
        print("2: Cadastro de Usarios")
=======
        print("2: Cadastro de Usarios (em produção)")
>>>>>>> a2877fe61eacd447534e3eddb950577193e86555
        print("3: Emprestimo (em produção)")
        print("4: Devolução (em produção)")
        print("5: Listar livros (em produção)")
        print("0: Sair")


        option = int(input("Select a option: ")) # Selecionador de opção

        if option == 1: #Criação de um livro
<<<<<<< HEAD
            coletar_dados_livro()

        elif option == 2:
            coletar_dados_usuario()

        elif option == 314: # Codigo debug se função carregar json funciona
            verificar_caminho()
            print("")
=======
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
            vericar_caminho()
>>>>>>> a2877fe61eacd447534e3eddb950577193e86555
            carregar_json()

        elif option == 0: # Fechamento do programa
            print("Adeus")
            break

        else: # Caso valor inserido em "option" seja diferente dos casos
            print("Tente novamente")


menu()
