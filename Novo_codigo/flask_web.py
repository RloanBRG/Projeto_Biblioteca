from flask import Flask, session
from python.Codigo_json import carregar_json, salvar_json
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if 'usuario' not in session:
            return redirect(url_for('login_home'))
        return f(*args, **kwargs)
    return decorated_function

app = Flask(__name__)
app.secret_key = "ajndiuoashudhih173y12y73y17"

from view import *

if __name__ == "__main__":
    app.run(debug=True)
    