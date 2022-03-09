import os
os.system('cls') or None

lista = [[], []]
for c in range(1, 8):
    n = int(input(f'{c}º Número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Lista completa: {lista}')
print(f'Pares: {lista[0]}')
print(f'Ímpares: {lista[1]}')
