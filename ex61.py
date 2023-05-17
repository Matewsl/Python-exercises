n1 = int(input('Digite o primeiro termo: '))
r = float(input('Qual a razão da PA?: '))
c = 1
#an = a1+(n-1).r
an=0
while c <= 10:
    an = n1+(c-1)*r
    print(f'{c}º Termo: {an}')
    c += 1