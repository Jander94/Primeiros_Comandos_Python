n = str(input('Nome completo: ')).strip()
nome = n.split()
print('O primeiro nome é {}'.format(nome[0]))
print('O ultimo nome é {}'.format(nome[len(nome) - 1]))
