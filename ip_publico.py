import socket
import requests
import json

# Mostar ip local
# ip_local = socket.gethostbyname(socket.gethostname()) # Coletando o ip local
# print(f'IP Local: {ip_local}')


# Mostar ip publico
ip_publico = requests.get('https://api.ipify.org/').text # Fazendo uma requsisão para a API que exibe o ip publico
print(f'IP Publico: {ip_publico}')
print(type(ip_publico)) # Exibindo o tipo de dado da variavel

# ip_publico = requests.get('https://api.ipify.org?format=json')
# ip_publico = ip_publico.json()
# ip_publico = ip_publico['ip']
# print(f'IP Publico: {ip_publico}')



# # Mostrar localição do ip
# localizacao = requests.get(f'https://geo.ipify.org/api/v2/country?apiKey=at_8SV4VBMSu0MJMlVPb5cryJIsg5GSk&ipAddress={ip_publico}') # fazendo uma requisição para a API de geolocalição por ip (retorna um json)
# localizacao = localizacao.json() # Convertento o json para um dicionario do python
# print(localizacao) # exibindo o dicionario na tela
# cidade = localizacao['location']['region'] # Recuperando um valor do dicionario
# print(cidade) # exibindo o valor recuperado do dicionario



localizacao = requests.get(f'https://api.techniknews.net/ipgeo/{ip_publico}') # API de geolocalização por ip gratuita
localizacao = localizacao.json()
# print(type(localizacao))
print(localizacao)
pais = localizacao['country']
cidade = localizacao['city']
dominio = localizacao['isp']
print(f'Pais: {pais}')
print(f'Cidade: {cidade}')
print(f'Dominio: {dominio}')
