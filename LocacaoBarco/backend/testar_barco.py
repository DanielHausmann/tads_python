from config import *
from declararBD import *

if __name__ == "__main__":

    if os.path.exists(arquivobd):
       db.session.query(Barco).delete()
    
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