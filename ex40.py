nomes = []
idade = []
idades, n , media = 0, 0, 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
qte_mulheres = 0
for c in range(0, 4):
    print(f'--- {c+1}ª PESSOA ---')
    nomes.append(input(f'Nome: '))
    idade.append(float(input('Idade: ')))
    sexo = input('Sexo [M/F]: ').lower()
    if sexo == 'm':
        if idade[c] > idade_homem_mais_velho:
            idade_homem_mais_velho = idade[c]
            nome_homem_mais_velho = nomes[c]
    elif sexo == 'f':
        if idade[c] < 20:
            qte_mulheres += 1
    n +=1
for c in range(0, 4):
    idades += idade[c]
media = idades/n
print('A média de idade do grupo é de {:.1f} anos'
      .format(media))
print(f'O homem mais velho tem {int(idade_homem_mais_velho)} '
      f'anos e se chama {nome_homem_mais_velho}.')
print(f'Ao todo são {int(qte_mulheres)} mulheres com '
      f'menos de 20 anos.')
