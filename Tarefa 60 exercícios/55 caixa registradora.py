while True:
    valor = 1
    i = 1
    total = 0
    while valor != 0:
        valor = float(input((f'{i}º Produto: ')))
        total += valor
        i += 1
    print(f'Total: R$ {total:.2f}')
    dinheiro = int(input('Dinheiro: '))
    troco = dinheiro - total
    print(f'Troco: R$ {troco}')
    print('-'*20)
