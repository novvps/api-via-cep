from libs.api import buscar_cep
from libs.banco import inserirInfo
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cep = request.form.get('cep')

        if not cep:
            return render_template('index.html', erro="Informe um CEP válido.")

        resultado = buscar_cep(cep)

        if not resultado:
            return render_template('index.html', erro="CEP não encontrado ou erro na API.")

        # Obtendo os dados retornados da API
        cepApi = resultado.get('cep', '')
        logradouro = resultado.get('logradouro', 'Não informado')
        complemento = resultado.get('complemento', 'Não informado')
        unidade = resultado.get('unidade', 'Não informado')
        bairro = resultado.get('bairro', 'Não informado')
        localidade = resultado.get('localidade', 'Não informado')
        uf = resultado.get('uf', '')
        estado = resultado.get('estado', 'Não informado')
        regiao = resultado.get('regiao', 'Não informado')
        ibge = resultado.get('ibge', '')
        gia = resultado.get('gia', '')
        ddd = resultado.get('ddd', '')
        siafi = resultado.get('siafi', '')

        # Inserindo no banco de dados
        inserirInfo(cepApi, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafi)

        # Renderiza a página com os dados
        return render_template('index.html', logradouro=logradouro, complemento=complemento, unidade=unidade, bairro=bairro, localidade=localidade, uf=uf, estado=estado, regiao=regiao, ibge=ibge, gia=gia, ddd=ddd, siafi=siafi)

    return render_template('index.html', logradouro='', complemento='', unidade='', bairro='', localidade='', uf='', estado='', regiao='', ibge='', gia='', ddd='', siafi='')  # Exibe a página inicial sem dados

if __name__ == '__main__':
    app.run(debug=True)