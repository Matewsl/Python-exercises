import random
print('Bem vindo ao Jokenpô do Mateus.\n'
      'Escolha 1 para Pedra\n'
      'Escolha 2 para Papel\n'
      'Escolha 3 para Tesoura\n')
jogador = int(input('Qual sua escolha? (Entre 1 e 3): '))
computador = random.randint(1,3)
# 1 ganha do 3
# 2 ganha do 1
# 3 ganha do 2
print('Você escolheu: {}'.format(jogador))
print('O computador escolheu {}'.format(computador))
#vencedor?
if jogador == computador:
      print('Deu empate! :)')
if jogador == 1 and computador == 2:
      print('Você perdeu!')
if jogador == 1 and computador == 3:
      print('Você ganhou!')
if jogador == 2 and computador == 1:
      print('Você Ganhou!')
if jogador == 2 and computador == 3:
      print('Você Perdeu!')
if jogador == 3 and computador == 1:
      print('Você Perdeu!')
if jogador == 3 and computador == 2:
      print('Você Ganhou!')
