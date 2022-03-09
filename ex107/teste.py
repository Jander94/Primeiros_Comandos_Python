import moeda
moeda.limpar()

v = float(input('Digite um valor: R$ '))

print(f'Aumentando 10% temos: R$ {moeda.aumentar(v, 10)}')
print(f'Diminuindo 20% temos: R$ {moeda.diminuir(v, 20)}')
print(f'O dobro é R$ {moeda.dobro(v)}')
print(f'A metade é R$ {moeda.metade(v)}')
