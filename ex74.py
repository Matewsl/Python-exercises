import random as r
a = r.randint(0, 50)
b = r.randint(0, 50)
c = r.randint(0, 50)
d = r.randint(0, 50)
e = r.randint(0, 50)
lista = (a, b, c, d, e)
menor = 1000
maior = 0
for c in lista:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'Números gerados: {lista}')
print(f'Maior: {maior}\n'
      f'Menor: {menor}')

