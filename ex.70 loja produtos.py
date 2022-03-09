from time import sleep
total = maismil = cont = menor = 0
barato = ''
while True:
    print('-'*30)
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        maismil += 1
    if cont == 1:
        barato = produto
        menor = preço
    if preço < menor:
        barato = produto
        menor = preço
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        print('\033[31mResposta incorreta.\033[m')
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    print('-'*30)
    if resp == 'N':
        print('Finalizando...')
        sleep(2)
        break
print('*'*30)
print(f'Valor da compra: R${total:.2f}')
print(f'{maismil} produtos custam mais de mil reais.')
print(f'O produto mais barato foi: {barato} custando R${menor:.2f}')
print('*'*30)
