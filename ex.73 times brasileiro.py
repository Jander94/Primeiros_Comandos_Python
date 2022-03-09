times = ('Atletico MG','flamengo','Palmeiras','Corinthians','Fortaleza', 'Bragantino',
'Fluminense','internacional','ceara','América','Cuiabá','santos','Atlético PR','São Paulo',
'Atletico GO','Juventude','Bahia','Gremio','Sport recife','Chapecoense')

#print(f'5 primeiros colocados: {times[:4]}')
print('5 primeiros colocados: ')
for  t in times[:5]:
    print(t, end=' ')

#print(f'\nUltimos 4 colocados: {times[16:]}')
print('\nUltimos 4 colocados: ')
for  t in times[-4:]:
    print(t, end=' ')
print('\n')

#Ordem alfabética
print(sorted(times))

p = input('Qual time vc quer saber a posição: ')
print(f'O {p} esta na {times.index(p)+1}ª posição.')

