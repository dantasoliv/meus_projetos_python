import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") # fazendo uma requisissão com a api de cotações (retorna um json)
cotacoes = cotacoes.json() # convertendo json para dicionario do python

moeda = input("""
    Digite umas das seguintes moedas para exibir a cotação em Real R$:
    dollar
    euro
    bitcoin
""")

#print(cotacoes) # Exibindo o json na tela
if(moeda == 'dollar'):
    print(f"Cotação do Dollar: {cotacoes['USDBRL']['bid']}")
elif(moeda == 'euro'):
    print(f"Cotação do Euro: {cotacoes['EURBRL']['bid']}")
elif(moeda == 'bitcoin'):
    print(f"Cotação do Bitcoin: {cotacoes['BTCBRL']['bid']}")
else:
    print('Opção Incorreta')
