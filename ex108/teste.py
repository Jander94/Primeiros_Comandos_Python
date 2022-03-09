import moeda
moeda.limpar()

v = float(input('Digite um valor: R$ '))

print(f'Aumentando 10% temos: {moeda.moeda(moeda.aumentar(v, 10))}')
print(f'Diminuindo 20% temos: {moeda.moeda(moeda.diminuir(v, 20))}')
print(f'O dobro é {moeda.moeda(moeda.dobro(v))}')
print(f'A metade é {moeda.moeda(moeda.metade(v))}')
