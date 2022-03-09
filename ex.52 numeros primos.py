'''n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
if cont > 2:
    print('\nNão é um número primo')
else:
    print('\nÉ um número primo')'''


n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end=' ')
        cont += 1
    else:
        print('\033[34m', end=' ')
    print(c, end=' ')
print('\no número {} foi divisível {} vezes'.format(n,cont))
if cont ==2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')

