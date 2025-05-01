from flask import redirect, url_for, render_template, request, session
from flask_web import app
from python.Codigo_json import carregar_json, salvar_json, verificar_caminho
from python.Usuarios import Usuario_Objeto
import re

verificar_caminho()

@app.route("/") #pagina inicial
def inicio():
    go_login = url_for("login_home")
    return render_template("home.html", click=go_login)

#pagina de login ou registro
@app.route("/login", methods=["GET","POST"]) #pagina de login
def login_home():

    if request.method == "POST":
        nome = request.form["nome"]
        idade = request.form["idade"]
        email = request.form["email"]
        senha = request.form["password"]
        acao = request.form["acao"]

        padrao_email = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(padrao_email, email):
            return render_template("login.html", mensagem="Email invalido", categoria="erro") 
        
        dados = carregar_json()

        # Registro
        if acao == "registro":
            for usuario in dados["Usuarios"]:
                if usuario["nome"] == nome:
                    return render_template("login.html", mensagem="Esse nome ja existe no banco de dados", categoria="erro")
            
            for usuario in dados["Usuarios"]:
                if usuario["email"] == email:
                    return render_template("login.html", mensagem="Esse email ja existe no banco de dados", categoria="erro")
            
            tipo = "comum"
            usuario_id = len(dados["Usuarios"]) + 1 # Adição de id com base no tamanho da lista de Usuario em json
            novo_usuario = Usuario_Objeto(usuario_id, nome, idade, email, senha, tipo)

            dados["Usuarios"].append(novo_usuario.para_dicionario())

            salvar_json(dados)
            return render_template("login.html", mensagem="Registro feito com sucesso", categoria="sucesso")

        for usuario in dados["Usuarios"]:
            if usuario['email'] == email and usuario['senha'] == senha:
                session['usuario'] = usuario['nome']
                session['tipo'] = usuario['tipo']

                return redirect(url_for('pagina_principal'))

        
        return render_template("login.html", mensagem = "Email ou senha invalidos", categoria="erro")


    return render_template("login.html")

@app.route("/perfil")
def perfil_usuario():
    return render_template("profile.html")

@app.route("/principal")
def pagina_principal():
    if 'usuario' not in session:
        return redirect(url_for('login_home'))
    dados = carregar_json()

    if dados is None:
        print("Erro em 'view.py'")
        return "Erro: dados não carregados"
        
    
    livros = dados["Livros"]
    voltar = url_for("inicio")


    return render_template("painel_principal.html", livros=livros, voltar=voltar, nome_usuario=session['usuario'])


@app.route("/listar_user")
def listar_user():

    dados = carregar_json()

    if dados is None:
        print("Erro em 'view.py'")
        return "Erro: dados não carregados"
        
    
    usuario = dados["Usuarios"]
    return render_template("pag_listar_user.html", usuario=usuario)


@app.route("/emprestimo")
def emprestimo_livros():
    return render_template("emprestimo.html")

@app.route("/edicao_livros")
def edicao_livros():
    return render_template()
