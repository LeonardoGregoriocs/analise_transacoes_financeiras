from app.models.models import db, Transactions

class Transacoes_repository:

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
