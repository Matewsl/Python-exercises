import time

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
op, result = 0, 0
numeros = []
while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
    print('[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior\n'
          '[4] novos números\n'
          '[5] sair do programa')
    op = int(input('Qual operação vc quer? '))
    if op == 1:
        result = n1+n2
        print(result)
    if op == 2:
        result = n1*n2
        print(result)
    if op == 3:
        if n1>n2:
            print(f'O maior é {n1}')
        elif n2>n1:
            print(f'O maior é {n2}')
        else:
            print(f'São iguais... {n1}')
    if op == 4:
        print('Mais oq? kkk.')
    if op == 5:
        print('Desligando tudo aqui..')
        time.sleep(1)
        print('Desligando tudo aqui......')
        time.sleep(1)
        print('\n')


print('fim')