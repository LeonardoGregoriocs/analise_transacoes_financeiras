import os

from app.models.models import db, User
from flask_bcrypt import generate_password_hash

class UserRepository:

    def new_user(nome, email, senha):
        new_user = User(
            nome=nome,
            email=email,
            senha=senha
        )

        db.session.add(new_user)
        db.session.commit()

    def create_admin():

        senha = generate_password_hash(os.environ['SENHA_ADMIN'])

        new_admin = User(
            nome="admin",
            email="admin@email.com.br",
            senha=senha
        )

        db.session.add(new_admin)
        db.session.commit()

    def get_all_user():
        return db.session.query(User).filter(User.nome != "admin").all()

    def get_user_id(id):
        user_obj = db.session.query(User).filter(User.id == id).first()
        return user_obj

    def update_user(nome, email, id):
        user_obj = db.session.query(User).filter(User.id == id).first()
        user_obj.nome = nome,
        user_obj.email = email

        db.session.commit()

    def delete_user(id):
        user_delete = db.session.query(User).filter(User.id == id).first()

        db.session.delete(user_delete)
        db.session.commit()

    def check_if_email_exists(email):
        return db.session.query(User).filter(User.email == email).first()
