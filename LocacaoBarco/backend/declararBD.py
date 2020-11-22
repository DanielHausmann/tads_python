from config import *

#Declara a Tabela Barco no Banco de Dados
class Barco(db.Model):
    
    id = db.Column(db.Integer,primary_key = True)
    cor = db.Column(db.String(254))
    ano = db.Column(db.Integer)
    tipo = db.Column(db.String(254))
    barcos = db.relationship('Locacoes',backref="barco",lazy="select") 
    def __str__(self):
        return str(self.id) + "," + self.tipo + "," + self.cor + "," + str(self.ano)   
    def json(self):
        return {
            "id" : self.id,
            "tipo" : self.tipo,
            "cor" : self.cor,
            "ano" : self.ano
        }

#Declara a Tabela Colaboradores no Banco de Dados
class Colaboradores(db.Model):
    
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    salario = db.Column(db.String(254))
    colaboradores = db.relationship('Locacoes',backref="colaboradores",lazy="select")
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

#Declara a Tabela Locacoes no Banco de Dados
class Locacoes(db.Model):
    
    id = db.Column(db.Integer,primary_key = True)
    cliente = db.Column(db.String(254))
    locacao = db.Column(db.String(254))
    dt_entrega = db.Column(db.String(254))
    id_barco = db.Column(db.Integer, db.ForeignKey('barco.id'))
    id_colaborador = db.Column(db.Integer, db.ForeignKey('colaboradores.id'))
    def __str__(self):
        return str(self.id) + "," + self.cliente + "," + self.locacao + "," + self.dt_entrega  + "," + str(self.id_barco) + "," + str(self.id_colaborador)
    def json(self):
        return {
            "id" : self.id,
            "cliente" : self.cliente,
            "data_locacao" : self.locacao,
            "data_entrega" : self.dt_entrega,
            "id_barco" : self.id_barco,
            "id_colaborador" : self.id_colaborador
        }        


if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    
    print("Banco de Dados declarado com sucesso!")