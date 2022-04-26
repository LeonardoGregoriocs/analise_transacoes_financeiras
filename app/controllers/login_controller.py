from flask import redirect, flash, session
from flask_bcrypt import check_password_hash

from app.repository.user_repository import UserRepository


class LoginController:

    def login(self, view, request):
        return redirect("/")

    def authenticate(self, view, request):
        try:
            email = request.form['email']
            senha = request.form['senha']

            user = UserRepository.check_if_email_exists(email)
            password = check_password_hash(user.senha, senha)

            if user and password:
                    session['usuario_logado'] = user.id
                    flash(f"{user.nome} logou com sucesso!")
                    return redirect("/importar-transacoes")
        except:
            flash("Usuário não logado, tente novamente!")
            return redirect('/')

    def logout(self, view, request):
        session['usuario_logado'] = None
        flash("Logout feito com sucesso!")
        return redirect('/')
