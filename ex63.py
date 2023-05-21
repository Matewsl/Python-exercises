print('-'*30)
print('Sequência de Fibonnaci\n' + '-'*30)
c = int(input('Quantos termos você quer ver: '))
n1 = 0
n2 = 0
n3 = n1 + n2
while c > 0:
    n3 = n2 + n1
    print(n3, '->', end=' ')
    n1 = n2
    n2 = n3
    c -=1
    if n2==0:
        n2 = 1

print('Fim =D')



# 0 > 1 > 1 > 2 > 3 > 5 > 8 > 13