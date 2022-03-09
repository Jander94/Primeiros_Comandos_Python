morango = int(input('Quantos Kg de morango: '))
maça = int(input('Quantos Kg de maça: '))
peso = morango + maça
valor = 0
if peso <= 5:
    preçomorango = 2.5
    preçomaça = 1.8
    valor = (morango * preçomorango) + (maça * preçomaça)

elif peso > 8 or valor > 25:
    preçomorango = 2.2
    preçomaça = 1.5
    valor = (morango * preçomorango) + (maça * preçomaça) - ((morango * preçomorango + maça * preçomaça) * 0.1)

elif peso > 5:
    preçomorango = 2.2
    preçomaça = 1.5
    valor = (morango * preçomorango) + (maça * preçomaça)

print(f'Você pagara R$ {valor:.2f} ')
