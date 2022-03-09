valor = int(input(('Valor da compra: R$ ')))
dinheiro = int(input('Valor entregue de dinheiro: R$ '))
troco = dinheiro - valor
print(f'Valor do troco: R$ {troco:.2f}')
cont100 = cont50 = cont20 = cont10 = cont5 = cont1 = 0
while troco != 0:
    if troco >= 100:
        troco -= 100
        cont100 += 1
    elif troco >= 50:
        troco -= 50
        cont50 += 1
    elif troco >= 20:
        troco -= 20
        cont20 += 1
    elif troco >= 10:
        troco -= 10
        cont10 += 1
    elif troco >= 5:
        troco -= 5
        cont5 += 1
    elif troco >= 1:
        troco -=1
        cont1 +=1
qtdnotas = cont1 + cont5 + cont10 + cont20 + cont50 + cont100

print(f'Serão necessário {qtdnotas} notas')
if cont100 > 0:
    print(f'{cont100} notas de R$100,00')
if cont50 > 0:
    print(f'{cont50} notas de R$50,00')
if cont20 > 0:
    print(f'{cont20} notas de R$20,00')
if cont10 > 0:
    print(f'{cont10} notas de R$10,00')
if cont5 > 0:
    print(f'{cont5} notas de R$5,00')
if cont1 > 0:
    print(f'{cont1} notas de R$1,00')

