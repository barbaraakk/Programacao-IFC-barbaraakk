from config import *
from pessoa import *

@app.route("/")
def ola():
    return "backend operante"

@app.route("/incluir_pessoa", methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        nova = Pessoa(**dados)
        db.session.add(nova)
        db.session.commit()
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})
    
@app.route("/listar_pessoas")
def listar_pessoas():
    try:
        lista = db.session.query(Pessoa).all()
        lista_retorno = [x.json() for x in lista]
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": lista_retorno})
        resposta = jsonify(meujson)
        return resposta
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})
