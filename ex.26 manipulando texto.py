frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira letra a esta na posição {}'.format(frase.find('a')+1))
print('A ultima letra A esta na posição {}'.format(frase.rfind('a')+1))
