import moeda
moeda.limpar()

v = float(input('Digite um valor: R$ '))

print(f'Aumentando 10% temos: {moeda.aumentar(v, 10, True)}')
print(f'Diminuindo 20% temos: {moeda.diminuir(v, 20, True)}')
print(f'O dobro é {moeda.dobro(v, True)}')
print(f'A metade é {moeda.metade(v, True)}')
