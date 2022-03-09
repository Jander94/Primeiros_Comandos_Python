p1 = int(input('Preço 1º produto: R$ '))
p2 = int(input('Preço 2º produto: R$ '))
p3 = int(input('Preço 3º produto: R$ '))
if p1 < p2 and p1 < p3:
    print('Você deve comprar o primeiro produto')
if p2 < p1 and p2 < p3:
    print('Você deve comprar o segundo produto')
if p3 < p2 and p3 < p1:
    print('Você deve comprar o terceiro produto')
