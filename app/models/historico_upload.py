from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class HistoricoUpload(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    data_transacao = db.Column(db.String(50), nullable=False)
    data_importacao = db.Column(db.DateTime, default=datetime.now())

    def new_record_upload(data_transacao):
        new_record_upload = HistoricoUpload(
            data_transacao=data_transacao
        )

        db.session.add(new_record_upload)
        db.session.commit()

    def get_information_transactions():
        return db.session.query(HistoricoUpload).filter(HistoricoUpload.data_importacao, HistoricoUpload.data_transacao).all()
