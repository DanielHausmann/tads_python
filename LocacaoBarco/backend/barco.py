from config import *
from declararBD import *

'''
class Barco(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    cor = db.Column(db.String(254))
    ano = db.Column(db.Integer)
    tipo = db.Column(db.String(254))
    def __str__(self):
        return str(self.id) + "," + self.tipo + "," + self.cor + "," + str(self.ano)   
    def json(self):
        return {
            "id" : self.id,
            "tipo" : self.tipo,
            "cor" : self.cor,
            "ano" : self.ano
        }
'''
'''
class Colaboradores(db.Model):
    
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    salario = db.Column(db.String(254))
    #colaboradores = db.relationship('Locacoes',backref="colaboradores",lazy="select")
    def __str__(self):
        return str(self.id) + "," + self.nome + "," + self.email + "," + self.telefone + "," + self.salario   
    def json(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "email" : self.email,
            "telefone" : self.telefone,
            "salario" : self.salario
        }
'''

if __name__ == "__main__":

    if os.path.exists(arquivobd):
       db.session.query(Barco).delete()
    
    #Inserindo Barcos no Banco de Dados
    exemplo1 = Barco(tipo="Iate",cor="azul",ano="2020")
    exemplo2 = Barco(tipo="caiaque",cor="vermelho",ano="2018")
    exemplo3 = Barco(tipo="lancha",cor="verde",ano="2015")
    exemplo4 = Barco(tipo="lancha",cor="verde",ano="2015")
    db.session.add(exemplo1)
    db.session.add(exemplo2)
    db.session.add(exemplo3)
    db.session.add(exemplo4)
    db.session.commit()
    todas = db.session.query(Barco).all()
    for p in todas:
        print(p)
        print(p.json())