import os

from flask import Flask
from mvc_flask import FlaskMVC


def create_app():
    app = Flask(__name__)
    FlaskMVC(app)

    app.secret_key=os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI']=os.environ["SQLALCHEMY_DATABASE_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]

    from app.models.transacoes import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.models.historico_upload import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
