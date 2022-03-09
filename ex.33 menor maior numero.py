a = int(input('Digite u número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))
# testando menor
menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
# Testando maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {} e o menor é {}.'.format(maior, menor))
