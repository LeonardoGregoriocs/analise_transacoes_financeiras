import os

from flask import Flask
from mvc_flask import FlaskMVC
from flask_bcrypt import Bcrypt

def create_app():
    app = Flask(__name__)
    FlaskMVC(app)
    Bcrypt(app)

    app.secret_key=os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI']=os.environ["SQLALCHEMY_DATABASE_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]

    from app.models.models import db
    from app.repository.user_repository import UserRepository
    db.init_app(app)

    with app.app_context():
        db.create_all()
        if not UserRepository.check_if_email_exists("admin@email.com.br"):
            UserRepository.create_admin()

    return app
