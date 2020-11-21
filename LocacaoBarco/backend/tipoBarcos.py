from config import *

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

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()
    

    exemplo1 = Barco(tipo="Iate",cor="azul",ano="2020")
    exemplo2 = Barco(tipo="caiaque",cor="vermelho",ano="2018")
    exemplo3 = Barco(tipo="lancha",cor="verde",ano="2015")
    db.session.add(exemplo1)
    db.session.add(exemplo2)
    db.session.add(exemplo3)
    db.session.commit()
    todas = db.session.query(Barco).all()
    for p in todas:
        print(p)
        print(p.json())
