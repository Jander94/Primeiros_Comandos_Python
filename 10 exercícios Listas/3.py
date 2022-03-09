cont =0
lista = []
while cont < 10:
    idade = int(input('Digite a idade: '))
    lista.append(idade)
    cont += 1
print(f'Maior Idade: {max(lista)}')
print(f'Menor Idade: {min(lista)}')
