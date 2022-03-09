valor = float(input('Preço do pão: R$ '))
for c in range (1, 51):
    print(f'{c} x {valor} = R$ {c*valor:.2f}')
    