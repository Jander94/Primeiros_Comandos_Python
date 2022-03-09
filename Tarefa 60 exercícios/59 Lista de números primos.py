numeros = []
primos = []
teste = []
cont = 0
n = int(input('Digite um número: '))
for c in range(2, n+1):
    numeros.append(c)
for x in range(2, n+1):
    teste.append(x)
for num in numeros:
    for t in teste:
        if num % t == 0:
            cont += 1
    if cont < 2:
        primos.append(num)
    cont = 0
print(f'Lista números: {numeros}')
print(f'Números Primo: {primos}')
