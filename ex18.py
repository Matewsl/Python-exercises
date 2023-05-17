casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite seu salário: R$ '))
anos = float(input('Em quantos anos vc vai pagar a casa? '))
meses=anos*12
prestacao = casa/meses
print('Prestação: {:.2f}'.format(prestacao))
if salario*0.3 >= prestacao:
    print('Financiamento aprovado!')
else:
    print('Financiamento recusado!')