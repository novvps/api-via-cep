from flask import Flask, render_template, request, redirect, url_for, jsonify, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_cep', methods=['POST'])
def buscar_cep_front():
    cep = request.form.get('cep')
    if not cep:
        return jsonify({'erro': 'CEP não informado'}), 400
    
    # Envia a requisição para o backend com o CEP digitado
    response = requests.get(f'http://127.0.0.1:7000/buscar_cep/{cep}')
    
    if response.status_code == 404:
        return jsonify({'erro': 'CEP inválido'}), 404

    # Retorna os dados para o frontend
    dados = response.json()
    
    return render_template('resultado.html', dados=dados)

@app.route('/todos_cep', methods=['GET'])
def todos_cep():
    requisicao = requests.get('http://127.0.0.1:7000/ver_tabela')
    if requisicao.status_code == 404:
        return jsonify({'erro': 'Nenhum dado encontrado'}), 404
    
    dados = requisicao.json()
    if dados == None:
        return render_template_string('<h1>Sem histórico de pesquisa</h1>')
    return render_template('todos_cep.html', dados=dados)
if __name__ == '__main__':
    app.run(debug=True, port=8000)
