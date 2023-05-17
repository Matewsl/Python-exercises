import math
import random

x = random.randint(0, 5)

t = int(input('Adivinhe o numero: '))

print('Acertou!' if t==x else 'Perdeu nb', x )