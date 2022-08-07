from app.models.models import *

class HistoricoUploadRepository:

    def new_record_upload(data_transacao, user_id, nome_usuario):
        new_record_upload = HistoricoUpload(
            data_transacao=data_transacao,
            user_id=user_id,
            nome_usuario=nome_usuario
        )

        db.session.add(new_record_upload)
        db.session.commit()

    def get_information_transactions():
        return db.session.query(HistoricoUpload).filter(
        HistoricoUpload.data_importacao,
        HistoricoUpload.data_transacao
        ).all()

    def get_information_transactions_details(id):
        return db.session.query(HistoricoUpload).filter(HistoricoUpload.id == id).filter(
        HistoricoUpload.data_importacao,
        HistoricoUpload.data_transacao
        ).all()

    def get_id(id):
        return db.session.query(HistoricoUpload).filter(HistoricoUpload.id == id).first()
