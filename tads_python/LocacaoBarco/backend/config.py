from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from flask_cors import CORS
import os
from flask import request
app = Flask(__name__)
CORS(app)
caminho = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(caminho,'locacaoBarco.db')
#Configurações do BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




