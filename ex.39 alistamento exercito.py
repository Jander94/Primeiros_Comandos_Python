from datetime import date
a = int(input('Que ano você nasceu: '))
i = date.today().year - a
print('Quem nasceu em {} tem {} anos'.format(a,i))
if i < 18:
    print('Faltam {} anos para você se alistar.'.format(18 - i))
    print('Seu alistamento será em {}'.format(date.today().year + (18-i)))
elif i == 18:
    print('Esta na idade de se alistar')
elif i > 18:
    print('Deveria ter se alistado a {} anos.'.format(i - 18))
    print('Seu alistamento foi em {}'.format(date.today().year - (i - 18)))
