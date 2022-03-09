resposta = 'S'
numeros = []
pares = []
impares = []
while resposta == 'S':
    numeros.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar?: ').upper()[0]

for p in numeros:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)

print(f'Lista completa: {numeros}\nPares: {pares}\nImpares: {impares}')
