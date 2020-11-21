from config import *
from tipoBarcos import Barco

@app.route("/")
def padrao():
    return "Funcionando....."

@app.route("/listar_barcos")
def listar_barcos():
    barcos = db.session.query(Barco).all()
    retorno = []
    for p in barcos:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

app.run(debug = True) 