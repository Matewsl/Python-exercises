n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo: '))
n3 = float(input('Digite o terceiro: '))

maior = 0.0
if n1 >= n2 and n1>=n3:
    maior=n1
elif n2>= n1 and n2>=n3:
    maior=n2
else:
    maior=n3

print('O maior é', maior)