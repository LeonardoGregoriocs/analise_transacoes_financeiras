import csv
import os

from flask import flash, redirect, render_template, session
from jsonschema import ValidationError

from app.repository.historico_upload_repository import HistoricoUploadRepository
from app.repository.transacoes_repository import Transacoes_repository
from app.repository.user_repository import UserRepository

DIRETORIO = os.environ['DIRETORIO']

class HomeController:
    def main_page(self, view, request):
        return render_template("login.html")

    def index(self, view, request):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            flash("Usuário não está logado!")
            return redirect('/')

        data = HistoricoUploadRepository.get_information_transactions()
        return render_template("index.html", dados=data)

    def upload_arquivo(self, view, request):
        file = request.files.get("file")

        try:
            validation = validate_csv(file)
            if validation:
                file.save(get_arquivo(file))
                with open(get_arquivo(file), mode='r', encoding='utf-8') as arq:
                    for line in csv.reader(arq, delimiter=','):
                        check_date = Transacoes_repository.check_date(line[7][0:10])
                        if check_date:
                            flash("Esse arquivo já foi inserido anteriormente!")
                            return redirect("/importar-transacoes")

                content_validation = file_size(file)
                if content_validation == 0:
                    flash("Arquivo vazio, selecione outro!")
                    return redirect("/importar-transacoes")
                else:
                    flash("Arquivo enviado com sucesso!")

                print(f"Nome do arquivo: {file.filename}")
                print(f"Tamanho do arquivo: {file_size(file)} megabyte")

                default_date = date_first_line(file)

                with open(get_arquivo(file), mode='r', encoding='utf-8') as arq:
                    for line in csv.reader(arq, delimiter=','):
                            try:
                                if line[7][0:10] == default_date:
                                    print(line)
                                    check_empty_field(line)
                                    Transacoes_repository.new_record(line[0], line[1], line[2], line[3], line[4], line[5], line[6], default_date)

                            except:
                                del line
                                flash("Alguns arquivos não foram salvos, pois estavam com datas divergêntes ou faltando informações!")


                user = UserRepository.get_user_id(session['usuario_logado'])
                HistoricoUploadRepository.new_record_upload(default_date, user.id, user.nome)

        except Exception:
            flash("Nenhum arquivo selecionado ou arquivo invalido!")
        return redirect("/importar-transacoes")

    def details_imports(self, view, request):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            flash("Usuário não está logado!")
            return redirect('/')
        return render_template("detalhe_importacoes.html")

def get_arquivo(file):
    file_address = os.path.join(DIRETORIO, file.filename)
    return file_address

def file_size(file):
    size = os.path.getsize(get_arquivo(file))
    converted_size = size / 1000000
    return converted_size

def validate_csv(file):
    if not file.filename.endswith('.csv'):
        raise ValidationError
    else:
        return True

def date_first_line(file):
    with open(get_arquivo(file), mode='r', encoding='utf-8') as arq:
        for line in csv.reader(arq, delimiter=','):
            first_date = line[7][0:10]
            return first_date

def check_empty_field(line):
    for position in line:
        if position != '':
            continue
        else:
            del line
    return line
