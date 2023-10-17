from os import path

import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bla")
def bla():
    df = pd.read_excel( 'dados_vendas.xlsx')
    lista = df.values.tolist()
    
    result = "<ul>"
    for item in lista:
        result += f'<li>{item[0]} - {item[1]} - {item[2]}</li>'
    result += "</ul>"

    return result