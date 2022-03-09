numeros = []
pares = []
impares = []
for c in range(1, 21):
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    if num % 2 != 0:
        impares.append(num)
print(f'Números: {numeros}')
pares.sort()
impares.sort()
print(f'Pares: {pares}')
print(f'Impares: {impares}')
