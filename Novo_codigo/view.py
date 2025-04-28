from flask import redirect, url_for, render_template, request
from flask_web import app
from python.Codigo_json import *
import re

@app.route("/")
def pagina_web():
    return redirect(url_for('login_home'))

@app.route("/login", methods=["GET","POST"])
def login_home():
    if request.method == "POST":
        email = request.form["email"]

        padrao_email = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(padrao_email, email):
            return render_template("login.html", mensagem="Email invalido") 
        
        dados = carregar_json()
        for usuario in dados["Usuarios"]:
            if usuario['email'] == email:
                return redirect(url_for('pagina_principal'))

        # if existe_usuario == False:
        return render_template("login.html", mensagem = "Email ou senha invalidos(debug: algum erro aconteceu)")


    return render_template("login.html")

@app.route("/teste")
def teste():
    return "voce me achou"

@app.route("/perfil")
def perfil_usuario():
    return render_template("profile.html")

@app.route("/principal")
def pagina_principal():
    verificar_caminho()
    dados = carregar_json()

    if dados is None:
        print("Erro em 'view.py'")
        return "Erro: dados não carregados"
        
    
    livros = dados["Livros"]
    return render_template("pag_principal.html", livros=livros)
