soma = 0
from time import sleep
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num%2==0:
        soma+=num
        print(f'Adicionado par: {num}')
        sleep(0.5)
print(f'O valor total dos pares deu: {soma}')