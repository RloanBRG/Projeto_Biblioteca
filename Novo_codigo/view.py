from flask import redirect, url_for, render_template, request, session
from flask_web import app, login_required
from python.Codigo_json import carregar_json, salvar_json
from python.Usuarios import Usuario_Objeto
import re #importação de autenticação de email ou algo do tipo

# Pagina inicial
@app.route("/") 
def inicio():
    go_login = url_for("login_home")
       
    return render_template("home.html", click=go_login)

# Pagina de login ou registro
@app.route("/login", methods=["GET","POST"])
def login_home():

    if 'usuario' in session:
        return redirect(url_for("painel_biblioteca"))

    voltar = url_for("inicio")

    if request.method == "POST":
        nome = request.form["nome"]
        idade = request.form["idade"]
        email = request.form["email"]
        senha = request.form["password"]
        acao = request.form["acao"]

        padrao_email = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(padrao_email, email):
            return render_template("login.html", mensagem="Email invalido", categoria="erro", voltar=voltar) 
        
        dados = carregar_json()

        # Registro (cadastro)
        if acao == "registro":
            for usuario in dados["Usuarios"]:
                if usuario["nome"] == nome:
                    return render_template("login.html", mensagem="Esse nome ja existe no banco de dados", categoria="erro",voltar=voltar)
            
            for usuario in dados["Usuarios"]:
                if usuario["email"] == email:
                    return render_template("login.html", mensagem="Esse email ja existe no banco de dados", categoria="erro",voltar=voltar)
            
            tipo = "comum"
            usuario_id = len(dados["Usuarios"]) + 1 # Adição de id com base no tamanho da lista de Usuario em json
            novo_usuario = Usuario_Objeto(usuario_id, nome, idade, email, senha, tipo)

            dados["Usuarios"].append(novo_usuario.para_dicionario())

            salvar_json(dados)
            return render_template("login.html", mensagem="Cadastro feito com sucesso", categoria="sucesso", voltar = voltar)

        #Login
        for usuario in dados["Usuarios"]:
            if usuario['email'] == email and usuario['senha'] == senha:
                session['usuario'] = usuario['nome']
                session['email'] = usuario["email"]
                session['tipo'] = usuario['tipo']

                return redirect(url_for('painel_biblioteca'))

        
        return render_template("login.html", mensagem = "Email ou senha invalidos", categoria="erro", voltar = voltar)

    
    #Visualização padrão
    return render_template("login.html", voltar = voltar)


# Painel da biblioteca
@app.route("/painel_biblioteca")
@login_required
def painel_biblioteca():
    voltar = url_for("inicio")
    sair = url_for('logout')

    emprestar = url_for("emprestar_livros")
    
    if 'usuario' not in session:
        return redirect(url_for('login_home'))
    dados = carregar_json()

    if dados is None:
        print("Erro em 'view.py'")
        return "Erro: dados não carregados"        
    
    livros = dados["Livros"]

    return render_template("painel_principal.html", emprestar=emprestar, livros=livros, voltar=voltar, sair=sair, nome_usuario=session['usuario'])

# Sair de um usuario especifico
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_home'))

# Emprestimo de livros
@app.route("/emprestar/<int:livro_id>", methods=["POST"])
@login_required
def emprestar_livros(livro_id):
    if "usuario" not in session:
        return "Usuario não autenticado"
    
    user_secao = session()
    dados = carregar_json()

    for livro in dados["Livros"]:
        if livro["id"] == livro_id and livro["quantidade"] > 0:
            if livro["quantidade"] == 0:
                livro["disponive"] = False
            livro["quantidade"] -= 1
            break
    else:
        return url_for("painel_biblioteca", mensagem="Erro: livro não encontrado", categoria_mensagem="erro")
    
    for usuario in dados["Usuarios"]:
        if usuario["nome"] == user_secao["usuario"] and usuario["email"] == user_secao['email']:
            usuario.setdefault("emprestado", []).append(livro_id)
            break

    salvar_json(dados)

    return redirect(url_for("painel_biblioteca", mensagem="Emprestimo feito com sucesso", categoria_mensagem="Sucesso"))

# Devolução de Livros
@app.route("/devolver_livros", methods=["POST"])
def devolver_livros():
    dados = carregar_json()

    if "usuario" not in session:
        return redirect(url_for("login_home"))

    usuario = None
    for u in dados['Usuarios']:
        if u['nome'] == usuario_logado:
            usuario = u
            break

    if livro_id not in usuario.get("emprestado", []):
        return render_template("painel_principal.html", livros=dados["Livros"], mensagem="Você não emprestou este livro!")

    usuario['emprestado'].remove(livro_id)

    for livro in dados['livros']:
        if livro['id'] == livro_id:
            if livro['disponivel'] == False:
                livro['disponivel'] = True
            livro['quantidade'] += 1
            break
    salvar_json(dados)

    return redirect(url_for("painel_biblioteca"))

# @app.route('/teste_painel')
# @login_required
# def teste_painel():
#     emprestar = emprestar_livros()
#     devolver = devolver_livros()
#     voltar = url_for("inicio")
#     sair = url_for('logout')
    
#     if 'usuario' not in session:
#         return redirect(url_for('login_home'))
#     dados = carregar_json()

#     if dados is None:
#         print("Erro em 'view.py'")
#         return "Erro: dados não carregados"        
    
#     livros = dados["Livros"]
#     return render_template("painel.html", livros=livros, voltar=voltar, sair=sair, nome_usuario=session['usuario'], devolver=devolver, emprestar=emprestar)

# Perfil do usuario (possiblilidade)
# @app.route("/perfil")
# def perfil_usuario():
#     return render_template("profile.html")

# # a decidir
# @app.route("/emprestimo")
# def emprestimo_livros():
#     return render_template("emprestimo.html")


# @app.route("/edicao_livros")
# def edicao_livros():
#     return render_template()


# @app.route("/listar_user")
# def listar_user():

#     dados = carregar_json()

#     if dados is None:
#         print("Erro em 'view.py'")
#         return "Erro: dados não carregados"
        
    
#     usuario = dados["Usuarios"]
#     return render_template("pag_listar_user.html", usuario=usuario)


