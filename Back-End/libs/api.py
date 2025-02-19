import requests
import json

def buscar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    retorno = requests.get(url)
    retorno = json.loads(retorno.text)
    return retorno