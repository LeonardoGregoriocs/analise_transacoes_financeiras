from app.models.models import db, HistoricoUpload

class HistoricoUploadRepository:

    def new_record_upload(data_transacao):
        new_record_upload = HistoricoUpload(
            data_transacao=data_transacao,
        )

        db.session.add(new_record_upload)
        db.session.commit()

    def get_information_transactions():
        return db.session.query(HistoricoUpload).filter(HistoricoUpload.data_importacao, HistoricoUpload.data_transacao).all()
