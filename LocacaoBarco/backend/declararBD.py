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


if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()


    #Listando todos os Colaboradores
    todosColaboradores = db.session.query(Colaboradores).all()
    for p in todosColaboradores:
        print(p)
        print(p.json())

    todosBarcos = db.session.query(Barco).all()
    for p in todosBarcos:
        print(p)
        print(p.json())