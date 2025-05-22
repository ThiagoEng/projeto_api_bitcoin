import requests
from tinydb import TinyDB

def extrair():
    # Extrai os dados da API
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()

def transformar(dados_json):
    # Transforma os dados extraídos
    valor = dados_json['data']['amount']
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda
    }
    return dados_transformados

def load(dados_transformados):
    # Carrega os dados do banco de dados
    db = TinyDB('db.json')
    db.insert(dados_transformados)
    print("Dados salvos com sucesso no banco de dados.")
          
          
if __name__ == "__main__":
    dados_json = extrair()
    dados_transformados = transformar(dados_json)
    load(dados_transformados)