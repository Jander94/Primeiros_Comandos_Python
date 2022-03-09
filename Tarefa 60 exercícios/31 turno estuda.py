turno = input('''Em que turno você estuda: 
[M] MATUTINO
[V] VESPERTINO
[N] NOTURNO
''').strip().upper()[0]
while turno not in 'MVN':
    print('Valor invválido. Tente novamente.')
    turno = input('Turno: ')
if turno == 'M':
    print('Bom dia!')
if turno == 'V':
    print('Boa tarde!')
if turno == 'N':
    print('Boa Noite!')
