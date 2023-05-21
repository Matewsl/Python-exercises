soma, num, count = 0,0,0
while True:
    num = int(input('Digite o número (999 para sair): '))
    if num == 999:
        break
    count += 1
    soma += num

print(f'A soma dos {count} valores deu {soma}')