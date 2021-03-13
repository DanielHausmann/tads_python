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
def listar_locacao():
    locacoes = db.session.query(Locacao).all()
    retorno = []
    for p in locacoes:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta


#Rota para a Inserção de Barcos
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


#Rota para a Inserção de Colaboradores
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


#Rota para a exclusao de colaboradores
@app.route("/excluir_colaborador/<int:colaborador_id>", methods=['DELETE'])
def excluir_colaborador(colaborador_id):
    resposta = jsonify({"resultado": "ok"})
    try:
        Colaboradores.query.filter(Colaboradores.id==colaborador_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro"})
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta


#Rota para a exclusao de Barcos
@app.route("/excluir_barco/<int:barco_id>", methods=['DELETE'])
def excluir_barco(barco_id):
    resposta = jsonify({"resultado": "ok"})
    try:
        Barco.query.filter(Barco.id==barco_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro"})
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta


#Rota para a exclusao de Locacao
@app.route("/excluir_locacao/<int:locacao_id>", methods=['DELETE'])
def excluir_locacao(locacao_id):
    resposta = jsonify({"resultado": "ok"})
    try:
        Locacao.query.filter(Locacao.id==locacao_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro"})
    resposta.headers.add("Access-Control-Allow-Origin","*")
    return resposta



app.run(debug = True) 
