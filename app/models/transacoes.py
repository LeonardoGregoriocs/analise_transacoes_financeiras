from flask_sqlalchemy import SQLAlchemy

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


    def check_date(data):
        return db.session.query(Transactions).filter(Transactions.data_transacao == data).first()


    def new_record(banco_origem, agencia_origem, conta_origem, banco_destino, agencia_destino, conta_destino, valor_transacao, data_transacao):
        new_record = Transactions(
            banco_origem=banco_origem,
            agencia_origem=agencia_origem,
            conta_origem=conta_origem,
            banco_destino=banco_destino,
            agencia_destino=agencia_destino,
            conta_destino=conta_destino,
            valor_transacao=valor_transacao,
            data_transacao=data_transacao
        )

        db.session.add(new_record)
        db.session.commit()
