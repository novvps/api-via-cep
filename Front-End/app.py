from flask import Flask, render_template, request, redirect, url_for, jsonify
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

if __name__ == '__main__':
    app.run(debug=True, port=8000)
