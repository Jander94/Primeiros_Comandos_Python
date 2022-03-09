print('\033[35m*'*20)
print('      TABUADA')
print('*'*20)
n = int(input('\033[31mEscolha um número: '))
for c in range(1, 11):
    print('\033[35m{} x {} = {}'.format(n, c, n*c))

