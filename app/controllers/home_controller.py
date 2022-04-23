import csv
import os

from flask import flash, redirect, render_template
from jsonschema import ValidationError

from app.models.transacoes import Transactions
from app.models.historico_upload import HistoricoUpload

DIRETORIO = os.environ['DIRETORIO']

class HomeController:
    def index(self, view, request):
        data = HistoricoUpload.get_information_transactions()
        return render_template("index.html", dados=data)

    def upload_arquivo(self, view, request):
        file = request.files.get("file")

        try:
            validation = validate_csv(file)
            if validation:
                file.save(get_arquivo(file))
                with open(get_arquivo(file), mode='r', encoding='utf-8') as arq:
                    for line in csv.reader(arq, delimiter=','):
                        check_date = Transactions.check_date(line[7][0:10])
                        if check_date:
                            flash("Esse arquivo já foi inserido anteriormente!")
                            return redirect("/")

                content_validation = file_size(file)
                if content_validation == 0:
                    flash("Arquivo vazio, selecione outro!")
                    return redirect("/")
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
                                    Transactions.new_record(line[0], line[1], line[2], line[3], line[4], line[5], line[6], default_date)

                            except Exception as e:
                                del line
                                flash("Alguns arquivos não foram salvos, pois estavam com datas divergêntes ou faltando informações!")

                HistoricoUpload.new_record_upload(default_date)

        except Exception as e:
            print(e)
            flash("Nenhum arquivo selecionado ou arquivo invalido!")
        return redirect("/")


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
