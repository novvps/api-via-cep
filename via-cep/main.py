from libs.api import buscar_cep
from libs.banco import 

def main():
    cep = input('Digite um CEP: ')
    resultado = buscar_cep(cep)
    cepApi = resultado['cep']
    logradouro = resultado['logradouro']
    complemento = resultado['complemento']
    unidade = resultado['unidade']
    bairro = resultado['bairro']
    localidade = resultado['localidade']
    uf = resultado['uf']
    estado = resultado['estado']
    regiao = resultado['regiao']
    ibge = resultado['ibge']
    gia = resultado['gia']
    ddd = resultado['ddd']
    siafi = resultado['siafi']
    
main()