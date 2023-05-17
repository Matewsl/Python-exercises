print('Bem vindo a calculadora de imc! ')
#imc = peso / altura²
peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso / (altura*altura)
print('Seu IMC:', imc)
if imc > 40:
    print('Obesidade mórbida')
elif imc > 30:
    print('Obesidade')
elif imc > 25:
    print('Sobrepeso')
elif imc > 18.5:
    print('Peso ideal')
else:
    print('Abaixo do peso')