import time

x, n, maior_numero, menor_numero,soma = 0, 1, 0, 100_000, 0
while n != 0:
    while n != 0:
        n = int(input('Digite qual valor quer adicionar: \n'
                      '[0] para sair: '))
        x = x+1
        if n > maior_numero:
            maior_numero = n
        if n < menor_numero and n != 0:
            menor_numero = n
        soma += n
x=x-1
media = soma/x
print('\n\n\n')
time.sleep(1)
print(f'O maior número foi: {maior_numero}\n'
      f'O menor número foi: {menor_numero}\n'
      f'Foram digitados {x} números\n'
      f'A média dos números foi: {media}')