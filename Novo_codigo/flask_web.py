from flask import Flask, session

app = Flask(__name__)
app.secret_key = "ajndiuoashudhih173y12y73y17"

from view import *

if __name__ == "__main__":
    app.run(debug=True)