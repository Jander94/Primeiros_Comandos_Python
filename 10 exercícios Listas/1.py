cont = 0
numeros = []
while cont < 5:
    num = int(input('Digite um número: '))
    numeros.append(num)
    cont += 1
print(f'lista: {numeros}')
numeros.sort()
print(f'Ordem crescente: {numeros}')
numeros.sort(reverse=True)
print(f'Ordem decrescente: {numeros}')
