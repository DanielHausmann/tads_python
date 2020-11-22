from config import *
#barcos = db.relationship('Locacoes',backref="barco",lazy="select")

class Locacoes(db.Model):
    __tablename__ = 'Locacoes'
    id = db.Column(db.Integer,primary_key = True)
    cliente = db.Column(db.String(254))
    dt_locacao = db.Column(db.String(254))
    dt_entrega = db.Column(db.String(254))
    id_barco = db.Column(db.Integer, db.ForeignKey('barco.id'))
    id_colaborador = db.Column(db.Integer, db.ForeignKey('colaboradores.id'))
    def __str__(self):
        return str(self.id) + "," + self.cliente + "," + self.dt_locacao + "," + self.dt_entrega  + "," + str(self.id_barco) + "," + str(self.id_colaborador)
    def json(self):
        return {
            "id" : self.id,
            "cliente" : self.cliente,
            "data locação" : self.dt_locacao,
            "data entrega" : self.dt_entrega,
            "id barco" : self.id_barco,
            "id colaborador" : self.id_colaborador
        }



if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()
    
#Inserindo Locações no Banco de Dados
    locacao1 = Locacoes(cliente = "Daniel",dt_locacao="21/11/2020",dt_entrega = "26/11/2020")
    db.session.add(locacao1)
    barco4 = Barco(tipo="Trawler",cor="amarelo",ano="2016")
    db.session.add(barco4)
    colaborador4 = Colaboradores(nome="Gabriel",email="Gabriel@bla.com",telefone="4444-4444",salario="7777")
    db.session.add(colaborador4)

    colaborador4.colaboradores.append(locacao1)
    barco4.barcos.append(locacao1)
    
    
    db.session.commit()
   
#Listando todas as Locações
    todasLocacoes = db.session.query(Locacoes).all()
    for p in todasLocacoes:
       # print(p)
        print(p.json())


    




