
# import arquivo
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from flask_cors import CORS
from datetime import datetime
from pycpfcnpj import cpfcnpj
from flask import Flask, jsonify
from project.arquivo import route_api

MD = Marshmallow()


app = Flask(__name__)
app.register_blueprint(route_api)
CORS(app)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Dados(db.Model):
    __tablename__ = "dados"

    # coluna ID
    id = db.Column(db.Integer, primary_key=True)

    # coluna CPF
    cpf = db.Column(db.String(11), nullable=False)

    # coluna private
    private = db.Column(db.Boolean(), nullable=False)

    # coluna incompleto
    incompleto = db.Column(db.Boolean(), nullable=False)
    # coluna data da última compra

    dta_ult_compra = db.Column(db.Date())
    # coluna ticket médio

    ticket_medio = db.Column(db.Float())
    # coluna ticket da última compra
    ticket_ult_compra = db.Column(db.Float())

    # coluna loja mais frequente (CNPJ)
    loja_frequente = db.Column(db.String(14))

    # coluna loja mais da última compra (CNPJ)
    loja_ult_compra = db.Column(db.String(14))

    def __init__(self, cpf="", private=False, incompleto=False, dta_ult_compra="", ticket_medio=0, ticket_ult_compra=0, loja_frequente="", loja_ult_compra=""):
        self.cpf = cpf
        self.private = private
        self.incompleto = incompleto
        self.dta_ult_compra = dta_ult_compra
        self.ticket_medio = ticket_medio
        self.ticket_ult_compra = ticket_ult_compra
        self.loja_frequente = loja_frequente
        self.loja_ult_compra = loja_ult_compra


class Cpf(fields.Field):
    ''' recebe o dado e limpa os caracteres '''

    def _deserialize(self, value, *args, **kwargs):
        computed_cpf = ''.join(filter(str.isdigit, value))
        return computed_cpf if cpfcnpj.validate(computed_cpf) and len(computed_cpf) == 11 else ""

    def _serialize(self, value, *args, **kwargs):
        return value


class Cnpj(fields.Field):
    ''' recebe o dado e limpa os caracteres '''

    def _deserialize(self, value, *args, **kwargs):
        computed_cnpj = ''.join(filter(str.isdigit, value))
        return computed_cnpj if cpfcnpj.validate(computed_cnpj) and len(computed_cnpj) == 14 else None

    def _serialize(self, value, *args, **kwargs):
        return value


class Dta(fields.Field):
    ''' recebe uma string e transforma em data '''

    def _deserialize(self, value, *args, **kwargs):
        return datetime.strptime(value, '%Y-%m-%d') if value not in ['NULL', ''] else None

    def _serialize(self, value, *args, **kwargs):
        return value


class PontoFlutuante(fields.Field):
    ''' recebe uma string no formato valor decimal e transfrma em float '''

    def _deserialize(self, value, *args, **kwargs):
        return float(value) if value not in ['NULL', ''] else None

    def _serialize(self, value, *args, **kwargs):
        return value


class DadosSchema(MD.Schema):
    cpf = Cpf(required=True)
    private = fields.Boolean(required=True)
    incompleto = fields.Boolean(required=True)
    dta_ult_compra = Dta()
    ticket_medio = PontoFlutuante()
    ticket_ult_compra = PontoFlutuante()
    loja_frequente = Cnpj()
    loja_ult_compra = Cnpj()

# rota para ver se o servidor está up


@app.route("/")
def server_true():
    return jsonify(start=True)
