import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt

API_KEY = 'SUA_CHAVE_DE_API'

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def obter_dados_clima(cidade):
    try:
        url = BASE_URL + f'q={cidade}&appid={API_KEY}&units=metric&lang=pt_br'
        resposta = requests.get(url)
        dados = resposta.json()

        if dados['cod'] != 200:
            print(f"Erro ao obter dados: {dados['message']}")
            return None

        return dados

    except Exception as e:
        print(f"Erro ao conectar à API: {e}")
        return None

def exibir_previsao(dados):
    cidade = dados['name']
    pais = dados['sys']['country']
    temperatura = dados['main']['temp']
    umidade = dados['main']['humidity']
    descricao = dados['weather'][0]['description']
    probabilidade_chuva = dados['clouds']['all']
    
    print(f"--- Previsão para {cidade}, {pais} ---")
    print(f"Temperatura: {temperatura}°C")
    print(f"Umidade: {umidade}%")
    print(f"Descrição: {descricao}")
    print(f"Probabilidade de chuva: {probabilidade_chuva}%")
    
    return temperatura, umidade, probabilidade_chuva

def plotar_dados(temperatura, umidade, probabilidade_chuva):
    labels = ['Temperatura (°C)', 'Umidade (%)', 'Prob. Chuva (%)']
    valores = [temperatura, umidade, probabilidade_chuva]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, valores, color=['orange', 'blue', 'gray'])
    plt.title("Dados Climáticos")
    plt.xlabel("Fatores")
    plt.ylabel("Valores")
    plt.show()

def previsao_clima():
    cidade = input("Digite o nome da cidade: ")
    dados = obter_dados_clima(cidade)
    
    if dados:
        temperatura, umidade, probabilidade_chuva = exibir_previsao(dados)
        plotar_dados(temperatura, umidade, probabilidade_chuva)
    else:
        print("Não foi possível obter os dados climáticos. Tente novamente.")

def previsao_multiplas_cidades(cidades):
    for cidade in cidades:
        print("\n")
        dados = obter_dados_clima(cidade)
        if dados:
            temperatura, umidade, probabilidade_chuva = exibir_previsao(dados)
        else:
            print(f"Não foi possível obter os dados climáticos para {cidade}.")

if __name__ == '__main__':
    print("Escolha uma opção:")
    print("1. Previsão para uma cidade")
    print("2. Previsão para várias cidades")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        previsao_clima()
    elif opcao == "2":
        cidades = input("Digite os nomes das cidades separados por vírgula: ").split(",")
        previsao_multiplas_cidades([cidade.strip() for cidade in cidades])
    else:
        print("Opção inválida.")
