# Gerador de Senha
import random

letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '1234567890'
caracteres_especiais = '!@#$%&*()-_/\+?'

def gerar_senha(s):
    letras_mn = '' # Letras Minusculas
    letras_ma = '' # Letras Maiusculas
    nm = '' # Números
    ca_esp = '' # Caracteres Especiais
    resto = '' # caractrres restantes

    if s < 8 or s > 20:
        print('A senha deve ter no minimo 8 caracteres e no maximo 20')
        return False
    elif s % 4 == 0:
        r = int(s / 4)

        for i in range(r): # preenchendo a senha com letras minusculas 
            letras_mn += random.choice(letras_minusculas)

        for i in range(r):# preenchendo a senha com letras maiusculas 
            letras_ma += random.choice(letras_maiusculas)

        for i in range(r): # preenchendo a senha com letras números 
            nm += random.choice(numeros)

        for i in range(r): # preenchendo a senha com caracteres especiais
            ca_esp += random.choice(caracteres_especiais)

        senha_forte = list(letras_mn+letras_ma+nm+ca_esp)  # Juntando todos os caractres em uma lista
        # print(senha_forte)

        random.shuffle(senha_forte) # Embaralhando os caractres da lista

        return "".join(senha_forte) # Juntando todos os caractres da lista para transforaer em uma string
    else:
        r = int(s / 4)
        r2 = s % 4

        for i in range(r): # preenchendo a senha com letras minusculas 
            letras_mn += random.choice(letras_minusculas)

        for i in range(r):# preenchendo a senha com letras maiusculas 
            letras_ma += random.choice(letras_maiusculas)

        for i in range(r): # preenchendo a senha com letras números 
            nm += random.choice(numeros)

        for i in range(r): # preenchendo a senha com caracteres especiais
            ca_esp += random.choice(caracteres_especiais)
        
        for i in range(r2): # preenchendo a senha com caracteres especiais
            resto += random.choice(caracteres_especiais)

        senha_forte = list(letras_mn+letras_ma+nm+ca_esp+resto)  # Juntando todos os caractres em uma lista
        # print(senha_forte)

        random.shuffle(senha_forte) # Embaralhando os caractres da lista

        return "".join(senha_forte) # Juntando todos os caractres da lista para transforaer em uma string
try:        
    n_caracteres = int(input('Informe a qtd de caractres para a senha (Min 8, Max 20): '))

    if gerar_senha(n_caracteres): # Verificando se o retorno da função é false ou se retornou algum valor
        print(f'Senha gerada com {len(gerar_senha(n_caracteres))} caracteres:\n{gerar_senha(n_caracteres)}')
except Exception as erro:
    print('Digite apenas numeros inteiros')