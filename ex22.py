print('\033[0:30:47m Este programa verifica se 3 medidas podem formar um triângulo\n'
      ' e qual seu tipo. Digite as medidas abaixo:')
a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))
#é um triângulo? - INICIO
triangulo=True
if a+b < c:
    triangulo=False
if b+c < a:
    triangulo=False
if a+c < b:
    triangulo=False
if triangulo==True:
    print('É um triangulo? SIM!')
#é um triangulo - FIM
#tipo de triângulo:
if triangulo == True:
    if a == b and b == c:
        print('Tipo: Equilátero!')
    elif a != b and b != c and c != a:
        print('Tipo: Escaleno')
    else:
        print('Tipo: Isosceles')
else:
    print('\nNão é um triangulo! não tem tipo!')