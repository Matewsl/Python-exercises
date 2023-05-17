d = float(input('Digite a distância da viagem (em km): '))
total=0.0
if d<=200:
    total=d*0.5
else:
    total=d*0.45

print('Total da viagem: R${:.2f}' .format(total))