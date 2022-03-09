num = (int(input('1º número: ')),
int(input('2º número: ')),
int(input('3º número: ')),
int(input('4º número: ')),
int(input('5º número: ')))
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O 3 foi digitado na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado.')
print('Os números pares foram: ')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')

