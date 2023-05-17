maior, menor, peso =0,0,0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}º Pessoa: '))
    if c == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}kg e \n'
      f'O menor peso foi {menor}kg ...')