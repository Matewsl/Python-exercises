flag = 999
n = 0
soma=0
x=0
while n != flag:
    if n!=flag:
        n = float(input('Digite o numero: '))
        soma += n
        x +=1

print(f'Foram digitados {x-1} números, e a \n'
      f'soma entre eles deu {soma-flag}')
