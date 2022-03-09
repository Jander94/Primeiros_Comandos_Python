lista = []
cont = 0
while cont < 10:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1
lista.sort(reverse=True)
print(f'Ordem decrescente: {lista}')
print(f'Maior nº: {max(lista)}')
print(f'Menor Nº: {min(lista)}')

