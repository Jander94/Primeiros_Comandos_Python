n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
numeros = [n1, n2, n3]
numeros.sort(reverse=True)
print('Ordem decrescente: ', end=' ')
for c in numeros:
    print(c, end=' ')


'''n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n1 > n2 and n1 < n3 or n1 < n2 and n1 > n3:
    meio = n1
if n2 > n1 and n2 < n3 or n2 < n1 and n2 > n3:
    meio = n2
if n3 > n1 and n3 < n2 or n3 < n1 and n3 > n2:
    meio = n3

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('Ordem decrescente: ',end=' ')
print(maior,end=' ')
print(meio,end=' ')
print(menor)'''
