from datetime import date
import time
nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - nasc
print('Calculando..')
time.sleep(1)
print('Calculando....')
time.sleep(1)
print('O atleta tem {} anos de idade'.format(idade))
time.sleep(1)
if idade > 25:
    print('Categoria: MASTER')
elif idade > 19 and idade <= 25:
    print('Categoria: SENIOR')
elif idade <= 19 and idade >14:
    print('Categoria: JUNIOR')
elif idade <=14 and idade >9:
    print('Categoria: INFANTIL')
elif idade <=9:
    print('Categoria: MIRIM')