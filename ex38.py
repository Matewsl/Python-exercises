from datetime import date
ano, maiores, menores, idade = 0,0,0,0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = date.today().year - ano
    print(f'Idade: {idade}')
    if idade >20:
        maiores +=1
    else:
        menores +=1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E também tivemos {menores} pessoas menores de idade')