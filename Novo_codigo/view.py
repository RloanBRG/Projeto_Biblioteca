from flask import redirect, url_for, render_template, request, session, flash, get_flashed_messages
from flask_web import app, login_required
from python.Codigo_json import carregar_json, salvar_json, verificar_caminho
from python.Usuarios import Usuario_Objeto
import re #importação de autenticação de email ou algo do tipo

# Pagina inicial
@app.route("/") 
def inicio():
    go_login = url_for("login_home")
    sair = url_for("logout")
       
    return render_template("home.html", click=go_login, sair=sair)

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
                session['usuario'] = {
                                    "nome": usuario["nome"], #salvando o usuario e impormações importantes para uso posterior
                                    "email": usuario["email"],
                                    "idade": usuario["idade"],

                                    }

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
    dados = carregar_json()
    if dados is None:
        print("Erro em 'view.py'")
        return "Erro: dados não carregados"        
    
    livros = dados["Livros"]
    usuario_logado = session["usuario"]
    livros_emprestados = []

    for usuario in dados["Usuarios"]:
        if usuario["nome"] == usuario_logado["nome"] and usuario["email"] == usuario_logado["email"]:
            emprestado_dict = usuario.get("emprestado", {})
            break
        else:
            emprestado_dict = {}

    for livro in livros:
        livro_id_str = str(livro["id"])
        if livro_id_str in emprestado_dict:
            livros_emprestados.append({
                "id": livro["id"],
                "titulo": livro["titulo"],
                "autor": livro["autor"],
                "ano": livro["ano"],
                "genero": livro["genero"],
                "quantidade_emprestada": emprestado_dict[livro_id_str]
            })


    return render_template("painel_principal.html", livros=livros, livros_emprestados=livros_emprestados, voltar=voltar, sair=sair, nome_usuario=usuario_logado["nome"])

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
        return redirect(url_for("login_home"))
    
    user_secao = session["usuario"]
    dados = carregar_json()

    livro = next((l for l in dados["Livros"] if l["id"] == livro_id), None)
    if not livro or livro["quantidade"] <= 0:
        flash("Erro: livro não encontrado para emprestimo","erro")
        return redirect(url_for("painel_biblioteca"))
    
    livro["quantidade"] -= 1
    if livro["quantidade"] == 0:
        livro["disponivel"] = False

    for usuario in dados["Usuarios"]:
        if usuario["nome"] == user_secao["nome"] and usuario["email"] == user_secao['email']:
            usuario.setdefault("emprestado", {})
            
            total_emprestado = sum(usuario["emprestado"].values())

            if total_emprestado >= 3:
                flash("Erro: limite de emprestimo de livros atingido", "erro")
                return redirect(url_for("painel_biblioteca"))
            livro_id_str = str(livro_id)
            usuario["emprestado"][livro_id_str] = usuario["emprestado"].get(livro_id_str, 0) +1
            break

    salvar_json(dados)

    flash("Emprestimo feito com sucesso", "sucesso")
    return redirect(url_for("painel_biblioteca"))

# Devolução de Livros
@app.route("/devolver_livros/<int:livro_id>", methods=["POST"])
def devolver_livros(livro_id):
    if "usuario" not in session:
        return redirect(url_for("login_home"))
    
    dados = carregar_json()
    user_secao = session["usuario"]
    livro_id_str = str(livro_id)

    livro = next((l for l in dados["Livros"] if l["id"] == livro_id), None)
    if not livro:
        flash("Erro: livro não encontrado para devolução", "erro")
        return redirect(url_for("painel_biblioteca"))
    
    for usuario in dados["Usuarios"]:
        if usuario["nome"] == user_secao["nome"] and usuario["email"] == user_secao["email"]:
            emprestado = usuario.get("emprestado", {})

            if livro_id_str not in emprestado or emprestado[livro_id_str] <= 0:
                flash("Erro: você não possui este livro", "erro")
                return redirect(url_for("painel_biblioteca"))

            emprestado[livro_id_str] -= 1
            if emprestado[livro_id_str] == 0:
                del emprestado[livro_id_str]

            livro["quantidade"] += 1
            if livro["quantidade"] > 0:
                livro["disponivel"] = True

            break
    salvar_json(dados)
    flash("Livro devolvido com sucesso", "sucesso")
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


