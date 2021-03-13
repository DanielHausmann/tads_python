from config import *
from declararBD import *
#Declara a Tabela Barco no Banco de Dados


class Barco(db.Model):
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer,primary_key = True)
    cor = db.Column(db.String(254))
    ano = db.Column(db.Integer)
    tipo = db.Column(db.String(254))
    #toString da classe Barco
    def __str__(self):
        return str(self.id) + "," + self.tipo + "," + self.cor + "," + str(self.ano)   
    #retorna a classe Barco em formato JSON
    def json(self):
        return {
            "id" : self.id,
            "tipo" : self.tipo,
            "cor" : self.cor,
            "ano" : self.ano
        }

if __name__ == "__main__":
    #apaga o BD para não repetir os dados
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    #Cria todas as tabelas
    db.create_all()
       
    
    
    #testa a classe Barco
    barco1 = Barco(tipo="Iate",cor="azul",ano="2020")
    barco2 = Barco(tipo="Caiaque",cor="vermelho",ano="2018")
    barco3 = Barco(tipo="Lancha",cor="verde",ano="2015")
    barco4 = Barco(tipo="Escuna",cor="amarelo",ano="2017")
    
    #Persiste os objetos da classe no BD
    db.session.add(barco1)
    db.session.add(barco2)
    db.session.add(barco3)
    db.session.add(barco4)
    db.session.commit()

    #Listando todos os Barcos em formato Json
    todas = db.session.query(Barco).all()
    for p in todas:
        print(p.json())


