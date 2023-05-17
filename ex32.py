n1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
an=0.0 #an = a1+(n-1).r
for c in range(1, 11):
    an = n1 + (c - 1) * r
    print('{}o Termo: {}'.format(c, an))