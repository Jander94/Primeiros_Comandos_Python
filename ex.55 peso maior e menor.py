maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Peso {}ª pessoa: '.format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print('O maior peso é {} e o menor peso é {}'.format(maior, menor))
