a = float(input('Digite o lado A do triângulo: '))
b = float(input('Digite o lado B: '))
c = float(input('Digite o lado C: '))
existe = True

if a+b < c:
    existe=False
if b+c < a:
    existe=False
if c+a < b:
    existe=False

print('Este triângulo existe' if existe else 'Não pode existir um triângulo com estas medidas :(')