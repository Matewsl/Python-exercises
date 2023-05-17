preco = float(input('Digite o preço do produto: R$ '))
condicao = int(input('Qual condicão do pagamento? \n'
                     '1 para A vista no Dinheiro(10% desconto)\n'
                     '2 para A vista no Cartão(5% desconto)\n'
                     '3 para parcelado\n'))
parcelado=0
if condicao == 1:
    print('A vista dinheiro (10% desconto)\nO valor do produto ficou R${:.2f}'.format(preco*0.9))
if condicao == 2:
    print('A vista cartão (5% desconto)\nO valor do produto ficou R${:.2f}'.format(preco*0.95))
if condicao == 3:
    parcelado = int(input('Quantas vezes no cartão? '))
if parcelado > 0:
    if parcelado >=3:
        print('Preço final (20% de juros): R${:.2f}\n'
              'Parcela {} vezes de: R${:.2f}'.format(preco*1.2, parcelado, (preco*1.2)/parcelado))
    elif parcelado >=1 and parcelado <3:
        print('Preço final (0% de juros): R${:.2f}\n'
              'Parcela {} vezes de : R${:.2f}'.format(preco, parcelado,(preco/parcelado)))



