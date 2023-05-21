import random
import time

senha = ''
temp = ''
maiuscula = 0
qte_letras = int(input('Quantas letras você quer na sua senha? '))
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w',
            'y', 'x', 'z']
simbolos = ['!', '@', '#', '$', '%', '/', '&', '*', '*', '-', 'ç']
for c in range(0, qte_letras):
    temp = random.choice(alfabeto)
    maiuscula = random.randint(0, 1)
    if maiuscula == 1:
        temp = temp.upper()
    else:
        temp = temp.lower()
    senha += temp
qte_simbolos = int(input('Quantos símbolos você quer na sua senha? '))
for c in range(0, qte_simbolos):
    temp = random.choice(simbolos)
    senha += temp
qte_numeros = int(input('Quantos numeros você quer na sua senha? '))
for c in range(0, qte_numeros):
    temp = random.randint(0, qte_numeros)
    senha += str(temp)
print('Tudo certo, estou gerando sua senha..')
time.sleep(1)
print('Tudo certo, estou gerando sua senha......')
time.sleep(3)
print(f'Aqui está a sua nova senha:\033[0:30:42m {senha} \033[0:30:m')
