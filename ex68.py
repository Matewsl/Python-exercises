import random
import time

print('=-'*14 + '\nVAMOS JOGAR PAR OU ÍMPAR\n' + '=-'*14)
n_usuario, usuario, n_computador, computador, resultado = 0, '', 0, '',0
while True:
    n_usuario = int(input('Diga um valor: '))
    usuario = input('Par ou Ímpar? [P/I]: ').upper()
    n_computador = random.randint(1, 30)
    computador = random.choice(['P', 'I'])
    resultado = n_computador + n_usuario
    print('=-'*14 + f'\nVocê jogou {n_usuario} e o computador jogou '
                   f'{n_computador}. Total: [{resultado}]', end=' ')
    if resultado % 2 == 0:
        print('PAR!')
        print('=-'*14)
        if usuario == 'P':
            print('\033[0:30:42m Você VENCEU!\33[0:30:m')
        else:
            print('\033[0:30:41m Você PERDEU!\33[0:30:m')
    else:
        print('IMPAR!')
        print('=-'*14)
        if usuario == 'I':
            print('\033[0:30:42m Você VENCEU!\33[0:30:m')
        else:
            print('\033[0:30:41m Você PERDEU!\33[0:30:m')
    x = input('\n\n\nPRESSIONE QUALQUER COISA PARA JOGAR NOVAMENTE!')
    print('Reiniciando jogo..')
    time.sleep(1)
    print('Reiniciando jogo....')
    print('\n\n\n\n\n\n\n\n')


