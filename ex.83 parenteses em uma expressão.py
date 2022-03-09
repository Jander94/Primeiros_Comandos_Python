exp = input('Digite a expressão: ')
cont1 = cont2 = 0
for p in exp:
    if p == '(':
        cont1 += 1
    if p == ')':
        cont2 += 1
if cont1 == cont2:
    print('Expressão Válida')
else:
    print('Expressão Inválida')
