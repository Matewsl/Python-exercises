import time

n1 = int(input('Digite o primeiro termo: '))
r = float(input('Qual a razão da PA?: '))
c = 1
#an = a1+(n-1).r
an=0
mais=''
while c <= 10:
    an = n1+(c-1)*r
    print(f'{c}º Termo: {an}')
    c += 1
x = c
while mais != 0:
    mais = int(input('Quer ver mais quantos termos?\n'
      '[0] para sair: '))
    for c in range(c, c+mais):
        an = n1+(c-1)*r
        print(f'{c}º Termo: {an}')
        c +=1
print('Desligando tudo...')
time.sleep(1)
print('fim')
