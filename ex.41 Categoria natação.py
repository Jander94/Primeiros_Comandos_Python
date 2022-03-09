from datetime import date
ano = int(input('Em que ano você nasceu: '))
idade = date.today().year - ano
if idade <= 9:
    print('{} anos, Categoria MIRIM'.format(idade))
elif idade <= 14:
    print('{} anos, Categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('{} anos, Categoria JUNIOR'.format(idade))
elif idade <= 20:
    print('{} anos, Categoria SENIOR'.format(idade))
else:
    print('{} anos, Categoria MASTER'.format(idade))
