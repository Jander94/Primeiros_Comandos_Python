numeros = []
for c in range(5):
    numeros.append(int(input(f'Numero: ')))
    if c == 0:
        mai = men = numeros[c]
    else:
        if numeros[c] > mai:
            mai = numeros[c]
        if numeros[c] < men:
            men = numeros[c]
print(f'Maior valor: {mai}, posição: ', end='')
for p, num in enumerate(numeros):
    if num == mai:
        print(p,end=' - ')
print()
print(f'\nmenor valor: {men}, posição: ', end='')
for p, num in enumerate(numeros):
    if num == men:
        print(p,end=' - ')

#Usando Index será informado apenas a primeira posição encontrada.

'''print(f'Maior valor: {max(numeros)} posição {numeros.index(max(numeros))}')
print(f'Menor valor: {min(numeros)} posição {numeros.index(min(numeros))}')'''
