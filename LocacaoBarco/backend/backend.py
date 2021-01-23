from config import *
from declararBD import *

#Rota padrão para verificar se a aplicação está funcionando
@app.route("/")
def padrao():
    return "Aplicação Funcionando."

#Rota para verificar a listagem de Barcos
@app.route("/listar_barcos")
def listar_barcos():
    barcos = db.session.query(Barco).all()
    retorno = []
    for p in barcos:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

#Rota para verificar a listagem de Colaboradores
@app.route("/listar_colaboradores")
def listar_colaboradores():
    colaboradores = db.session.query(Colaboradores).all()
    retorno = []
    for p in colaboradores:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

#Rota para verificar a listagem de Locações
@app.route("/listar_locacoes")
def listar_locacoes():
    locacoes = db.session.query(Locacoes).all()
    retorno = []
    for p in locacoes:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

@app.route("/incluir_barco",methods=['post'])
def incluir_barco():
    
    dados = request.get_json()
    print(dados)
    novo_barco = Barco(**dados) 
    db.session.add(novo_barco)
    db.session.commit()
    return {"resultado" : "ok"}
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta


@app.route("/incluir_colaborador",methods=['post'])
def incluir_colaborador():
    
    dados = request.get_json()
    print(dados)
    novo_colaborador = Colaboradores(**dados) 
    db.session.add(novo_colaborador)
    db.session.commit()
    return {"resultado" : "ok"}
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta

app.run(debug = True) 
