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

class Colaboradores(db.Model):
    __table_args__ = {'extend_existing': True} 
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


if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()
       
    
    
    #Inserindo Barcos no Banco de Dados
    barco1 = Barco(tipo="Iate",cor="azul",ano="2020")
    barco2 = Barco(tipo="Caiaque",cor="vermelho",ano="2018")
    barco3 = Barco(tipo="Lancha",cor="verde",ano="2015")
    barco4 = Barco(tipo="Escuna",cor="amarelo",ano="2017")
    #Inserindo Colaboradores no Banco de Dados
    colaborador1 = Colaboradores(nome="João",email="Joao@bla.com",telefone="1111-1111",salario="6050")
    colaborador2 = Colaboradores(nome="Miguel",email="Miguel@bla.com",telefone="2222-2222",salario="7000")
    colaborador3 = Colaboradores(nome="Theago",email="Theago@bla.com",telefone="3333-3333",salario="10000")
    colaborador4 = Colaboradores(nome="Nicolas",email="Nicolas@bla.com",telefone="4444-4444",salario="8800")
    
    db.session.add(barco1)
    db.session.add(barco2)
    db.session.add(barco3)
    db.session.add(barco4)
    db.session.add(colaborador1)
    db.session.add(colaborador2)
    db.session.add(colaborador3)
    db.session.add(colaborador4)
    db.session.commit()
    todas = db.session.query(Barco).all()
    #Listando todos os Barcos em formato Json
    for p in todas:
        print(p.json())
    
    #Listando todos os Colaboradores em formato Json
    todosColaboradores = db.session.query(Colaboradores).all()
    for p in todosColaboradores:
        print(p.json())