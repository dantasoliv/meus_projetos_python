import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") # fazendo uma requisissão com a api de cotações (retorna um json)
cotacoes = cotacoes.json() # convertendo json para dicionario do python
cotacao_dolar = cotacoes['USDBRL']['bid']

#print(cotacoes) # Exibindo o json na tela
print(cotacao_dolar)

