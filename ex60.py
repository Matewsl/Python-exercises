import math
n = int(input('Numero: '))
c = n
print(f'{n}!=', end='')
while c > 0:
    if c == 1:
        print(f'{c}=', end='')
    if c != 1:
        print(f'{c}x', end='')
    c -= 1
fat = math.factorial(n)
print(fat)