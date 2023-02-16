from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def padrao():
    return '''Exemplo de servidor que retorna lista. Ações:
    <a href="/lista_texto">Lista em texto</a> | 
    <a href="/lista_json">Lista em json</a>'''

@app.route("/lista_texto")
def lista_texto():
    lista = ['ola', 'esta lista', 'vai ser mostarda', 'em formato', 'textual']
    retorno = ''

    for s in lista:
        retorno += "<br>"
        retorno += s

    return retorno

@app.route("/lista_json")
def lista_json():
    lista = ['sera que', 'voce vai gostar', 'da lista em json?', 'veremos', ':-)']

    return jsonify(lista)

app.run()

