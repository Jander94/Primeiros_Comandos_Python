n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
n3 = float(input('3ª nota: '))
media = (n1+n2+n3)/3
if media == 10:
    print(f'Media: {media}\nAprovado com distinção')
elif media >= 7:
    print(f'Média: {media}\nAprovado')
elif media < 7:
    print(f'Média: {media}\nReprovado')

