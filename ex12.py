vel = int(input('Digite a velocidade: '))
multa = (vel-80)*7
print('Dentro do limite!' if multa<=0
      else 'Você foi multado em R${:.2f}'
      .format(multa))
