# Gerador de Senha
import random

letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '1234567890'
caracteres_especiais = '!@#$%&*()-_/\+?'

letras_mn = '' # Letras Minusculas
letras_ma = '' # Letras Maiusculas
nm = '' # Números
ca_esp = '' # Caracteres Especiais


for i in range(3): # preenchendo a senha com letras minusculas 
    letras_mn += random.choice(letras_minusculas)

for i in range(3):# preenchendo a senha com letras maiusculas 
    letras_ma += random.choice(letras_maiusculas)

for i in range(3): # preenchendo a senha com letras números 
    nm += random.choice(numeros)

for i in range(3): # preenchendo a senha com caracteres especiais
    ca_esp += random.choice(caracteres_especiais)

senha_forte = list(letras_mn+letras_ma+nm+ca_esp)  # Juntando todos os caractres em uma lista
print(senha_forte)

random.shuffle(senha_forte) # Embaralhando os caractres da lista

print("".join(senha_forte)) # Juntando todos os caractres da lista para transforaer em uma string