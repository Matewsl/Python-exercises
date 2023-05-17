n = int(input('Digite um número inteiro: '))
while n > 100:
    n = int(input('Inválido! \nPor favor, digite um número abaixo de 100: '))
primo=True
for c in range(2, 101):
    if n != c:
        if n%c == 0:
            primo=False

print(f'O número {n} é PRIMO' if primo else f'O número {n} não é primo')
