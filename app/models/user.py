from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(150))
    senha = db.Column(db.String(150))

    def new_user(nome, email, senha):
        new_user = User(
            nome=nome,
            email=email,
            senha=senha
        )

        db.session.add(new_user)
        db.session.commit()

    def create_admin():
        new_admin = User(
            nome="admin",
            email="admin@email.com.br",
            senha='123999'
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
