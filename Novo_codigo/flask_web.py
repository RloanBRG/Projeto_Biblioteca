from flask import Flask
from python.Codigo_json import *

app = Flask(__name__)

from view import *

if __name__ == "__main__":
    app.run(debug=True)