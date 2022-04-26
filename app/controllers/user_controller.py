import os
import random
import smtplib

from flask import redirect, render_template, flash, session
from flask_bcrypt import Bcrypt
from email.message import EmailMessage

from app.models.user import User

EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

class UserController:

    def register(self, view, request):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            flash("Usuário não está logado!")
            return redirect('/')

        return render_template('cadastro.html')

    def user_registered(self, view, request):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            flash("Usuário não está logado!")
            return redirect('/')
        user_registered = User.get_all_user()
        return render_template("usuarios.html", users=user_registered)

    def new_register(self, view, request):
        try:
            name = request.form['name']
            email = request.form['email']
            senha = str(random.randint(100000, 999999))

            if name == '':
                flash("O campo nome não pode ficar vazio")
                return redirect("/cadastro")
            if email == '':
                flash("O campo e-mail não pode ficar vazio")
                return redirect("/cadastro")

            email_exists = User.check_if_email_exists(email)
            if not email_exists:

                password_hash = password_encrypted(senha)

                User.new_user(nome = name, email = email, senha=password_hash)
                flash("Cadastro feito com sucesso! Será enviado uma senha pro seu e-mail")

                send_email(email=email, name=name, password=senha)

                return redirect('/cadastro')

        except Exception as e:
            print(e)
        flash("E-mail já cadastrado em nossa base de dados!")
        return redirect("/cadastro")

    def edit_register(self, view, request, id):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            flash("Usuário não está logado!")
            return redirect('/')
        return render_template('editar.html')

    def update_user(self, view, request, id):
        user_obj = User.get_user_id(id)

        user_obj.name = request.form['name']
        user_obj.email = request.form['email']

        if user_obj.name == '':
            flash("O campo nome não pode ficar vazio")
            return redirect("cadastro")
        if user_obj.email == '':
            flash("O campo e-mail não pode ficar vazio!")
            return redirect("cadastro")

        User.update_user(user_obj.name, user_obj.email, id)

        return redirect('/usuarios')


    def delete_user(self, view, request, id):
        User.delete_user(id)

        flash(f"Usuário com ID: {id} removido com sucesso!")
        return redirect('/usuarios')

def password_encrypted(password):
    bcrypt = Bcrypt()
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    return password_hash

def send_email(email, name, password):
    msg = EmailMessage()
    msg['Subject'] = 'Senha para acesso'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg.set_content(f"Olá {name}! Sua senha para acesso é: {password}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
