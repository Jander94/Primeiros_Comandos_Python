cont = 0
p1 = input('Telefonou para a vítima: ').upper()[0]
if p1 == 'S':
    cont += 1
p2 = input('Esteve no local do crime: ').upper()[0]
if p2 == 'S':
    cont += 1
p3 = input('Mora perto da vítima: ').upper()[0]
if p3 == 'S':
    cont += 1
p4 = input('Devia para a vítima: ').upper()[0]
if p4 == 'S':
    cont += 1
p5 = input('Já trabalhou com a vítima: ').upper()[0]
if p5 == 'S':
    cont += 1
print('Classificação: ',end=' ')
if cont == 2:
    print('Suspeita')
elif 3 <= cont <= 4:
    print('Cumplice')
elif cont == 5:
    print('Assassino')
elif cont <= 1:
    print('Inocente')
