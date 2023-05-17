import time
from random import randint
play_again = True
while play_again == True:
    numero_secreto = randint(0, 10)
    tentativas = 1
    x=0
    print('Adivinhe um número entre 0 e 10')
    palpite = int(input('Palpite: '))
    while palpite != numero_secreto:
            if palpite < numero_secreto:
                tentativas += 1
                print('Incorreto! O número é MAIOR!')
            elif palpite > numero_secreto:
                tentativas +=1
                print('Incorreto! O número é MENOR!')
            palpite = int(input('Palpite: '))
    print('Parabéns! Você acertou!')
    print(f'O número é {numero_secreto}')
    print(f'Você ganhou com {tentativas} tentativas.')
    while x != 's' and x != 'n':
        x = input('Deseja jogar novamente? [S/N]').lower()
        if x == 'n':
            play_again = False
            print('Obrigado por jogar! Volte sempre! xD')
            print('Desligando o sistema..')
            time.sleep(1)
            print('Desligando....')
        elif x == 's':
            play_again = True
            print('Reiniciando..')
            time.sleep(1)
            print('Reiniciando.....')
            time.sleep(1)
print('Fim :)')
