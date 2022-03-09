numeros = []
for c in range(20):
    n = int(input('Digite um número: '))
    numeros.append(n)

print(f'Números: {numeros}')
numeros.pop(2)
print(f'Números 2.0: {numeros}')
