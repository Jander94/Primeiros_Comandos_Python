frase = str(input('Digite uma frase: ')).upper()
junto = frase.replace(' ', '')
cont = frase[::-1].upper().replace(' ', '')
print('A frase digitada ao contrário é: {}.'.format(cont))
if str(junto) == str(cont):
    print('É um palindromo')
else:
    print('Não é um palindromo')

