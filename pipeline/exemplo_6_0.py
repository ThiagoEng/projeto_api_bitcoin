import requests
from tinydb import TinyDB
from datetime import datetime
import time

def extrair():
    # Extrai os dados da API
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()

def transformar(dados_json):
    # Transforma os dados extraídos
    valor = dados_json['data']['amount']
    valor = dados_json['data']['amount']
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    dados_tratados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": datetime.now().isoformat()  # Adiciona o timestamp atual
    }
    return dados_tratados

def load(dados_tratados):
    # Carrega os dados do banco de dados
    db = TinyDB('db.json')
    db.insert(dados_tratados)
    print("Dados salvos com sucesso no banco de dados.")
          
          
if __name__ == "__main__":
    while True:
        dados_json = extrair()
        dados_tratados = transformar(dados_json)
        load(dados_tratados)
        time.sleep(15)  