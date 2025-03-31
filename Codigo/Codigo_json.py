from Livros import Livro_Objeto
from Usuarios import Usuario_Objeto
import json
import os

pasta_projeto = os.path.dirname(os.path.abspath(__file__)) # Verica onde o arquivo esta localizado no computador
caminho_json = os.path.join(pasta_projeto, "biblioteca.json") # Verica se existe um biblioteca para ser adionado no diretorio

def verificar_caminho():
     print(f"o caminho da pasta é {pasta_projeto}")
     print("")
     print(f"O caminho do JSON é {caminho_json}")


def carregar_json(): # Carregar informações do arquivo biblioteca.json
        try:
            with open(caminho_json, "r", encoding="utf-8") as f:
                return json.load(f)               
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado")
        except json.JSONDecodeError:
            print("Erro: não foi possivel decodificar o arquvo json")

def salvar_json(dados): # Salvamento de dados
     with open(caminho_json, "w", encoding="utf-8") as f:
          json.dump(dados, f, indent=4, ensure_ascii=False)

def coletar_dados_livro(): # Função que atuará na criação e salvamento de um livro no arquivo json
    dados = carregar_json()

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

    livro_id = len(dados["Livros"]) + 1 # Adição de id com base no tamanho da lista de livros em json
    novo_livro = Livro_Objeto(livro_id, titulo, ano, genero, autor, disponivel)
 
    dados["Livros"].append(novo_livro.para_dicionario())

    salvar_json(dados)
    print(f"O livro '{titulo}' foi adicionado, mas será que foi?")

def coletar_dados_usuario(): # Função que atuará na criação e salvamento de um usuario no arquivo json
    dados = carregar_json()

    nome = input("Digite o Nome: ")
  
    while True: #Loop de verificação se input é um digito
        idade = input("Qual a sua idade? (somente numeros): ")
        if idade.isdigit():
            break
        else: # Caso não
            print("Valor inserido não é um numero")

    email = input("Qual o seu email?: ")
    print("Qual o tipo desse usuario?")

    while True:
        selecionar_tipo = input("Selecione uma das opções:\n(1 - Comum | 2 - autor | 3 - administrador): ")
        if selecionar_tipo == "1":
            tipo = "comum"
            break
        elif selecionar_tipo == "2":
            tipo = "autor"
            break
        elif selecionar_tipo == "3":
            tipo = "adm"
            break
        else:
            print("Valor inserido invalido")

    usuario_id = len(dados["Usuarios"]) + 1 # Adição de id com base no tamanho da lista de Usuario em json
    novo_usuario = Usuario_Objeto(usuario_id, nome, idade, email, tipo)
 
    dados["Usuarios"].append(novo_usuario.para_dicionario())

    salvar_json(dados)
    print(f"O Usuario '{nome}' foi adicionado, mas será que foi?")
    #confirmando modificações