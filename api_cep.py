import requests
import json

meu_cep = input("Digite seu CEP:")

cep = requests.get("https://cep.awesomeapi.com.br/json/"+meu_cep) # Conectando com a API de CEP (Vai retornar um arquivo Json)
print(cep)
resposta_cep = str(cep)
# print(type(resposta_cep))
if (resposta_cep == '<Response [400]>'):
    print('CEP não encontrado')
else:
    cep = cep.json() # convertendo para o resultado da cxonsulta da API de CEP do formato json para dicionario do Python
    # print(type(cep))
    rua = cep['address_name']
    tipo = cep['address_type']
    bairro = cep['district']
    cidade = cep['city']

    print(cep)
    print(tipo+": "+rua)
    print("Bairro:",bairro)
    print("Cidade:",cidade)