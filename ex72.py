entrada_usuario = 0
numeros_por_extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    entrada_usuario = int(input('Digite um número(0 a 10): '))
    while entrada_usuario < 0 or entrada_usuario > 10:
        entrada_usuario = int(input('Entrada inválida, digite um número (0 a 10): '))
    print(f'Você digitou {numeros_por_extenso[entrada_usuario]}')