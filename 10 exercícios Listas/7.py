numeros = []
for c in range(10):
    n = int(input('Digite um número: '))
    numeros.append(n)
print(f'Números: {numeros}')
numeros.insert(1, 10)
print(f'Números 2.0: {numeros}')
