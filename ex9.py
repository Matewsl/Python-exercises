frase = input('Digite uma frase: ')
x = frase.lower().count('a')
first = frase.index('a')

print('Na frase {}, a letra "a" aparece: {} vezes\n'
      'A primeira vez no index: {}'.format(frase, x, first))
