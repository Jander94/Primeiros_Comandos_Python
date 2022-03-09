print('='*30)
print('{:^30}'.format('BANCO ITAÚ'))
print('='*30)
v = int(input('Informe o Valor a sacar: R$ '))
ced = 50
totced = 0
while True:
    if v >= ced:
        v -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if v == 0:
            break
print('='*30)
