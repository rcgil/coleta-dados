import re
import threading
from flask import jsonify, Blueprint
from flask_cors import CORS

route_api = Blueprint('route_api', __name__)
# teste = DadosSchema()


@route_api.route("/process-file")
def process_file():

    # abre e carrega o arquivo
    with open("base_teste.txt", 'r') as file:
        lines = file.readlines()[1:]

    iteration = 1
    start = 0
    insertThreads = []
    # Cria uma thread a cada 5000 linhas
    for step in range(5000, len(lines), 5000):
        insertThreads.append(
            threading.Thread(
                target=thread_cleanup,
                args=("thread_"+str(iteration), lines[start:step])))
        if step+5000 > len(lines):
            insertThreads.append(
                threading.Thread(
                    target=thread_cleanup,
                    args=("thread_"+str(iteration+1), lines[start+5001: len(lines)])))

        start = step
        iteration += 1

    for t in insertThreads:
        t.start()

    for t in insertThreads:
        t.join()

    return jsonify(len(lines))


def thread_cleanup(thread_name, data):
    try:
        from dados import DadosSchema, Dados, db
    except ImportError:
        import sys
        dados = sys.modules[__package__ + 'dados']

    print("Iniciando thread %s" % thread_name)
    cleanup_data = []

    for i in range(len(data)):
        # trata os valores decimais removendo as vígulas
        # remove os espaços e cria linhas os dados separados por vígulas
        # cria um array com os dados
        novo_registro = re.sub(
            '\s+', ',', re.sub(',', '.', data[i]))[:-1].split(',')
        # se o array contém um número diferente de 8 posições ignora essa iteração
        if len(novo_registro) != 8:
            print(novo_registro)
            continue
        # cria os jsons para validação do marshmallow
        cleanup_data.append({
            "cpf": novo_registro[0],
            "private": novo_registro[1],
            "incompleto": novo_registro[2],
            "dta_ult_compra": novo_registro[3],
            "ticket_medio": novo_registro[4],
            "ticket_ult_compra": novo_registro[5],
            "loja_frequente": novo_registro[6],
            "loja_ult_compra": novo_registro[7]
        })
    # carrega a lista de json no validador do marshmallow
    # Valida cada json transformando para o modelo de dados
    linhas_processadas = DadosSchema(many=True).load(cleanup_data)
    insere_linhas = []
    for linha in linhas_processadas:
        # carrega todos os dados em um array com o modelo de Dados
        insere_linhas.append(
            Dados(
                cpf=linha["cpf"],
                private=linha["private"],
                incompleto=linha["incompleto"],
                dta_ult_compra=linha["dta_ult_compra"],
                ticket_medio=linha["ticket_medio"],
                ticket_ult_compra=linha["ticket_ult_compra"],
                loja_frequente=linha["loja_frequente"],
                loja_ult_compra=linha["loja_ult_compra"]
            )
        )

    # insere os dados na base
    db.session.add_all(insere_linhas)
    db.session.commit()
    print("Finalizando thread %s" % thread_name)
