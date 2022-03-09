import os
os.system("cls") or None

princ = []
lista = []
mai = menor = 0
    #Coletar dados
while True:
    lista.append(input('Nome: '))
    lista.append(float(input('Peso: ')))
    #Analisar maior e menor peso  e adicionar a lista principal
    if len(princ) == 0:
        mai = menor = lista[1]
    else:
        if lista[1] > mai:
            mai = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    princ.append(lista[:])
    lista.clear()
    res = input('Quer continuar?: ').upper()[0]
    if res in 'Nn':
        break
    #imprimir os resultados
print('*-'*30)
print(f'Foram cadastrados: {len(princ)} pessoas')
print(f'O maior peso foi {mai}', end=' ')
    #identificar nomes do maior peso
for c in princ:
    if c[1] == mai:
        print(c[0],end=' ')

print(f'\nO menor peso foi {menor}',end=' ')
    #identificar nomes do menor peso
for c in princ:
    if c[1] == menor:
        print(c[0], end=' ')
