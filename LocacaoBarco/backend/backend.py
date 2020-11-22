from config import *
from declararBD import *

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

@app.route("/listar_colaboradores")
def listar_colaboradores():
    colaboradores = db.session.query(Colaboradores).all()
    retorno = []
    for p in colaboradores:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

@app.route("/listar_locacoes")
def listar_locacoes():
    locacoes = db.session.query(Locacoes).all()
    retorno = []
    for p in locacoes:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

app.run(debug = True) 