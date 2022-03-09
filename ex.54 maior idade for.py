from datetime import date
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Ano de nascimento {}ª pessoa: '.format(c)))
    if date.today().year - ano < 18:
        menor += 1
    else:
        maior += 1
print('{} pessoas já são de maior idade, e {} ainda são de menor idade.'.format(maior, menor))
