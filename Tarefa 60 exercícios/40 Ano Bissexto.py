ano = int(input('Digite um ano: '))
if ano % 4 == 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto')
elif ano % 100 == 0:
    print(f'O ano {ano} não é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto')

