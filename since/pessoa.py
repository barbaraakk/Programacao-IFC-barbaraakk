from config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    email = db.Column(db.Text)
    telefone = db.Column(db.Text)

    def __str__(self):
            return f'{self.nome}, ' +\
                f'{self.email}, {self.telefone}'

    def json(self):
            return {
                "nome": self.nome,
                "email": self.email,
                "telefone": self.telefone
        }
