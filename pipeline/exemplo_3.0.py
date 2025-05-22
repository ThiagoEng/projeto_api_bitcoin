import requests


def extrair():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()

def transformar(dados):
    valor = dados['data']['amount']
    criptomoeda = dados['data']['base']
    moeda = dados['data']['currency']
    dados_transformados = {
        'valor': valor,
        'criptomoeda': criptomoeda,
        'moeda': moeda
    }
    return dados_transformados

if __name__ == "__main__":
    dados = extrair()
    dados_transformados = transformar(dados)
    print(dados_transformados)