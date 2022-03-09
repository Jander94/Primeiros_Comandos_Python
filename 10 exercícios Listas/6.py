numeros = []
repetidos = []
quantas = []
for c in range(10):
    n = int(input('Digite um número: '))
    numeros.append(n)
    qtd = numeros.count(n)
    if qtd > 1:
        if n not in repetidos:
            repetidos.append(n)
for r in repetidos:
    quantas = numeros.count(r)
    print(f'{r} repetiu {quantas} vezes')

