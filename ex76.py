lista = ('oi','Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('------------------------------------------------\n'
      '{:^50}'.format('LISTAGEM DE PREÇOS'))
print('------------------------------------------------')
for c in range(1, len(lista)):
    if c%2 != 0: #Impar
        x=''
        x+=str(lista[c])
        while len(x)<25:
            x += '.'
        print(f'{x}..............', end='')
    if c%2 == 0: #par
        s = ' '
        x2 = lista[c]
        if lista[c] < 10:
            s = '   '
        elif lista[c] < 100:
            s = '  '
        else:
            s = ' '
        print(f'R${s}{lista[c]:.2f}')