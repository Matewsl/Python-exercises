soma=0
cap = 0
for c in range(1, 501, 2):
    if c%3==0:
        soma += c
        print('Valor c:', c, 'Total atual: ', soma)
        cap += 1

print('A soma deu ', soma, '| Foram capturados {} valores'.format(cap))
