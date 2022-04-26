from flask import redirect, flash, session
from flask_bcrypt import check_password_hash

from app.models.user import User


class LoginController:

    def login(self, view, request):
        return redirect("/")

    def authenticate(self, view, request):
        email = request.form['email']
        senha = request.form['senha']

        user = User.check_if_email_exists(email)
        password = check_password_hash(user.senha, senha)

        if user and password:
                session['usuario_logado'] = user.id
                flash(f"{user.nome} logou com sucesso!")
                return redirect("/importar-transacoes")
        else:
            flash("Usuário não logado, tente novamente!")
            return redirect('/')

    def logout(self, view, request):
        session['usuario_logado'] = None
        flash("Logout feito com sucesso!")
        return redirect('/')
