from config import *
from declararBD import *

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
        db.session.query(Colaboradores).delete()

    db.create_all()
    
#Inserindo Colaboradores no Banco de Dados
    colaborador1 = Colaboradores(nome="João",email="Joao@bla.com",telefone="1111-1111",salario="2050")
    colaborador2 = Colaboradores(nome="Miguel",email="Miguel@bla.com",telefone="2222-2222",salario="3000")
    colaborador3 = Colaboradores(nome="Theago",email="Theago@bla.com",telefone="3333-3333",salario="10000")
    colaborador4 = Colaboradores(nome="Nicolas",email="Nicolas@bla.com",telefone="4444-4444",salario="2800")
    db.session.add(colaborador1)
    db.session.add(colaborador2)
    db.session.add(colaborador3)
    db.session.add(colaborador4)
    db.session.commit()

#Listando todos os Colaboradores
    todosColaboradores = db.session.query(Colaboradores).all()
    for p in todosColaboradores:
        print(p)
        print(p.json())