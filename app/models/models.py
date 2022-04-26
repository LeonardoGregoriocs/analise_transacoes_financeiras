from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Transactions(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    banco_origem = db.Column(db.String(50), nullable=False)
    agencia_origem = db.Column(db.String(50), nullable=False)
    conta_origem = db.Column(db.String(50), nullable=False)
    banco_destino = db.Column(db.String(50), nullable=False)
    agencia_destino = db.Column(db.String(50), nullable=False)
    conta_destino = db.Column(db.String(50), nullable=False)
    valor_transacao = db.Column(db.String(50), nullable=False)
    data_transacao = db.Column(db.String(50), nullable=False)

class User(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(150))
    senha = db.Column(db.String(150))

class HistoricoUpload(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    data_transacao = db.Column(db.String(50), nullable=False)
    data_importacao = db.Column(db.DateTime, default=datetime.now())
    id_user = db.Column(db.Integer)
