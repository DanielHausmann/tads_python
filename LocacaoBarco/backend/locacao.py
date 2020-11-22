from config import *
from declararBD import *

if __name__ == "__main__":

    if os.path.exists(arquivobd):
          db.session.query(Locacoes).delete()

    db.create_all()
    
    #Inserindo Locações no Banco de Dados
    locacao1 = Locacoes(cliente = "Daniel",locacao="21/11/2020",dt_entrega = "26/11/2020")
    locacao2 = Locacoes(cliente = "Gabriel",locacao="12/12/2020",dt_entrega = "27/12/2020")
    locacao3 = Locacoes(cliente = "Gustavo",locacao="02/01/2021",dt_entrega = "05/01/2021")
    db.session.add(locacao1)
    db.session.add(locacao2)
    db.session.add(locacao3)
    barcoEscolhido = Barco.query.filter_by(ano="2018").first()
    colaboradorEscolhido = Colaboradores.query.filter_by(nome="Theago").first()
    #atribuindo as 2 chaves estrangeiras na tabela Locacoes
    colaboradorEscolhido.colaboradores.append(locacao1)
    barcoEscolhido.barcos.append(locacao1)

    barcoEscolhido = Barco.query.filter_by(ano="2020").first()
    colaboradorEscolhido = Colaboradores.query.filter_by(nome="Miguel").first()
    colaboradorEscolhido.colaboradores.append(locacao2)
    barcoEscolhido.barcos.append(locacao2)

    barcoEscolhido = Barco.query.filter_by(ano="2017").first()
    colaboradorEscolhido = Colaboradores.query.filter_by(nome="João").first()
    colaboradorEscolhido.colaboradores.append(locacao3)
    barcoEscolhido.barcos.append(locacao3)
      
    db.session.commit()
   
    #Listando todas as Locações em formato Json
    todasLocacoes = db.session.query(Locacoes).all()
    for p in todasLocacoes:
        print(p.json())


    




