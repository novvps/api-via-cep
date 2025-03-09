from flask import Flask, jsonify
from libs.api import buscar_cep
from libs.banco import inserirInfo
from libs.banco import verTabela
app = Flask(__name__)

@app.route('/buscar_cep/<cep>', methods=['GET'])
def buscar(cep):
    # Chama a função que busca o CEP
    retorno = buscar_cep(cep)
    
    # caso o retorno falhe
    if not retorno:
        return jsonify({'erro': 'CEP inválido'}), 404 # erro

    dados = retorno
    if dados:
        inserirInfo(
            cep=dados.get('cep'),
            logradouro=dados.get('logradouro'),
            complemento=dados.get('complemento'),
            unidade=dados.get('unidade'),
            bairro=dados.get('bairro'),
            localidade=dados.get('localidade'),
            uf=dados.get('uf'),
            estado=dados.get('estado'),
            regiao=dados.get('regiao'),
            ibge=dados.get('ibge'),
            gia=dados.get('gia'),
            ddd=dados.get('ddd'),
            siafi=dados.get('siafi')
        )
    # Retorna as informações no formato JSON
    return jsonify(retorno)

@app.route('/ver_tabela', methods=['POST', 'GET'])
def ver_tabela():
    dados = verTabela()  # Obtém os dados do banco
    dados_formatados = []

    for item in dados:
        dados_formatados.append({
            "cep": item[0],
            "logradouro": item[1],
            "complemento": item[2],
            "unidade": item[3],
            "bairro": item[4],
            "localidade": item[5],
            "uf": item[6],
            "estado": item[7],
            "regiao": item[8],
            "ibge": item[9],
            "gia": item[10],
            "ddd": item[11],
            "siafi": item[12]
        })

    return jsonify(dados_formatados)


if __name__ == '__main__':
    app.run(debug=True, port=7000)