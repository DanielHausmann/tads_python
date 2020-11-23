from config import *
   
#Declara a Tabela Barco no Banco de Dados
class Barco(db.Model):
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer,primary_key = True)
    cor = db.Column(db.String(254))
    ano = db.Column(db.Integer)
    tipo = db.Column(db.String(254))
    #barcos = db.relationship('Locacoes',backref="barco",lazy="select") 
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
       
    
    
    #Inserindo Barcos no Banco de Dados
    exemplo1 = Barco(tipo="Iate",cor="azul",ano="2020")
    exemplo2 = Barco(tipo="Caiaque",cor="vermelho",ano="2018")
    exemplo3 = Barco(tipo="Lancha",cor="verde",ano="2015")
    exemplo4 = Barco(tipo="Escuna",cor="amarelo",ano="2017")
    
    db.session.add(exemplo1)
    db.session.add(exemplo2)
    db.session.add(exemplo3)
    db.session.add(exemplo4)
    db.session.commit()
    todas = db.session.query(Barco).all()
    #Listando todos os Barcos em formato Json
    for p in todas:
        print(p.json())
    