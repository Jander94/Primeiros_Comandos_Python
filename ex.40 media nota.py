n1 = float(input('Primeira nota: '))
n2 = float(input(('Segunda nota: ')))
m = (n1 + n2) / 2
if m < 5:
    print('Reprovado. média de {:.2f}'.format(m))
elif m < 6.9:
    print('Recuperação. média de {:.2f}'.format(m))
else:
    print('Aprovado. média de {:.2f}'.format(m))
