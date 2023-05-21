n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
n3 = int(input('Valor 3: '))
n4 = int(input('Valor 4: '))
n5 = int(input('Valor 5: '))
nove, tres, pares = 0, 0, 0
lista = (n1, n2, n3, n4, n5)
#A
for c in lista:
    if c == 9:
        nove += 1
    if c == 3:
        tres +=1
    if c % 2 == 0:
        pares +=1
print(f'Números digitados: {lista}')
print(f'O nove foi digitado {nove} vezes' if nove != 0 else 'Não apareceu nenhum 9')
print(f'O três foi digitado {tres} vezes' if tres != 0 else 'Não apareceu nenhum 3')
print(f'Foram digitados {pares} números pares' if pares != 0 else 'Não teve nenhum par')