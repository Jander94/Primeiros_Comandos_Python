resp = 'S'
cont = 1
temperaturas = []
soma = 0
while resp in 'S':
    temp = int(input(f'{cont}ª temperatura: ºC '))
    soma += temp
    cont += 1
    temperaturas.append(temp)
    resp = input('Quer continuar?: ').upper()[0]
print(f'Temperaturas coletadas: {temperaturas}')
print(f'Maior: {max(temperaturas)}')
print(f'Menor: {min(temperaturas)}')
print(f'Média: {soma/(cont-1)}')
