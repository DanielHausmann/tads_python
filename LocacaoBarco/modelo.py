from config import *

class Barco(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    placa = db.Column(db.String(254))
    ano = db.Column(db.Integer)
    tipo = db.Column(db.String(254))
    def __str__(self):
        return str(self.id) + "," + self.tipo + "," + self.placa + "," + str(self.ano)   
    def json(self):
        return {
            "id" : self.id,
            "tipo" : self.tipo,
            "placa" : self.placa,
            "ano" : self.ano
        }

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    novo = Barco(tipo="Iate",placa="VEL1234",ano="2020")
    db.session.add(novo)
    db.session.commit()
    todas = db.session.query(Barco).all()
    for p in todas:
        print(p)
        print(p.json())
