from Livros import Livro_Objeto
from Usuarios import Usuario_Objeto
import json
import os

pasta_projeto = os.path.dirname(os.path.abspath(__file__)) # Verica onde o arquivo esta localizado no computador
caminho_json = os.path.join(pasta_projeto, "biblioteca.json") # Verica se existe um biblioteca para ser adionado no diretorio
# Função debug (teste)
def verificar_caminho():
    print(f"o caminho da pasta é {pasta_projeto}")
    print("")
    print(f"O caminho do JSON é {caminho_json}")

# Função 1
def carregar_json(): # Carregar informações do arquivo biblioteca.json
        try:
            with open(caminho_json, "r", encoding="utf-8") as f:
                return json.load(f)               
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado")
        except json.JSONDecodeError:
            print("Erro: não foi possivel decodificar o arquvo json")

# Função 2
def salvar_json(dados): # Salvamento de dados
    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Função 3
def coletar_dados_livro(): # Função que atuará na criação e salvamento de um livro no arquivo json
    dados = carregar_json()

    titulo = input("Digite o Titulo: ")

    while True: #Loop de verificação se input é um digito
        ano = input("Qual o ano de lançamento? (somente numeros): ")
        if ano.isdigit():
            int(ano)
            break
        else: # Caso não
            print("Valor inserido não é um numero")

    genero = input("Qual o genero do livro? (Ex: ação, misterio, romance...): ")
    autor = input("Qual o nome do autor do livro?: ")
    
    while True:
        quantidade = input("Quantos livros estarão disponiveis?: ")
        if quantidade.isdigit():
            int(quantidade)
            break
        else:
            print("Valor inserido não é um numero")

    if quantidade != "0":
        disponivel = True
    else:
        disponivel = False

    livro_id = len(dados["Livros"]) + 1 # Adição de id com base no tamanho da lista de livros em json
    novo_livro = Livro_Objeto(livro_id, titulo, ano, genero, autor, disponivel, quantidade)

    dados["Livros"].append(novo_livro.para_dicionario())

    salvar_json(dados)
    print(f"O livro '{titulo}' foi adicionado, mas será que foi?")

# Função 4
def coletar_dados_usuario(): # Função que atuará na criação e salvamento de um usuario no arquivo json
    dados = carregar_json()

    nome = input("Digite o Nome: ")

    while True: #Loop de verificação se input é um digito
        idade = input("Qual a sua idade? (somente numeros): ")
        if idade.isdigit():
            int(idade)
            break
        else: # Caso não
            print("Valor inserido não é um numero")

    email = input("Qual o seu email?: ")
    print("Qual o tipo desse usuario?")

    while True: # Selecionador de tipo de usuario
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


# Função 5
def listar_dados_livro(): #Listagem dos livros
    dados = carregar_json()
    if not dados["Livros"]:
        print("Nenhum livro cadastrado")
        return
    
    print("--- Livros na lista ---")
    print("")
    for livros in dados["Livros"]:
        print(f"ID : {livros['id']}")
        print(f"Titulo : {livros['titulo']}")
        print(f"Ano : {livros['ano']}")
        print(f"Genero : {livros['genero']}")
        print(f"Autor : {livros['autor']}")

        if livros['disponivel'] == True:
            print(f"Quantidade Disponivel {livros.get('quantidade', 1)}")
        else:
            print("O livro não esta disponivel para emprestimo")

        print("-"*40)


# Função 6        
def listar_dados_usuario(): #Listagem dos livros
    dados = carregar_json()
    if not dados["Usuarios"]:
        print("Nenhum Usuario cadastrado")
        return
    
    print("--- Usuarios na lista ---")
    print("")
    for usuarios in dados["Usuarios"]:
        print(f"ID : {usuarios['id']}")
        print(f"Nome : {usuarios['nome']}")
        print(f"Email : {usuarios['email']}")
        print(f"Idade : {usuarios['idade']}")
        print(f"Tipo : {usuarios['tipo']}")

        print("-"*40)

def emprestimo_livro():
    dados = carregar_json()
    print("Qual livro voce quer emprestar?")
    listar_dados_livro()
    
    while True:
        livro_id = input("digite o id: ")
        if livro_id.isdigit():
            int(livro_id)
            break
        else:
            print("Valor inserido não é um numero")

    for livros in dados["Livros"]:
        if livros['id'] == int(livro_id):
            if livros['quantidade'] > 0 and livros['disponivel'] == True:
                livros['quantidade'] -= 1
                if livros['quantidade'] == 0:
                    livros['disponivel'] = False
                salvar_json(dados)
                print(f"O livro {livros['titulo']} foi emprestado")
            
            else:
                print(f"Um {livros['titulo']} já foi emprestado")
                return
    print(f"Não foi encontrado um Livro com ID {livro_id}")

def devolver_livro():
    dados = carregar_json()

    print("Qual livro voce quer devolver?")
    listar_dados_livro()
    
    while True:
        livro_id = input("digite o id: ")
        if livro_id.isdigit():
            int(livro_id)
            break
        else:
            print("Valor inserido não é um numero")

    for livros in dados["Livros"]:
        if livros['id'] == int(livro_id):
            if livros['quantidade'] == 0 and livros['disponivel'] == False:
                livros['quantidade'] += 1
                salvar_json(dados)
                print(f"O livro {livros['titulo']} foi devolvido")
            
            else:
                print(f"Um {livros['titulo']} já foi devolvido")
                return
    print(f"Não foi encontrado um Livro com ID {livro_id}")
