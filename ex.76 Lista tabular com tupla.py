lista = ('Lapis', 1.5, 'caneta', 2.5, 'caderno', 16.90, 'mochila', 67.99, 'livro', 37.89)
print('-'*40)
print(f'{"LISTA ESCOLAR":^40}')
print('-'*40)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end=' ')
    else:
        print(f'R$ {lista[c]:.2f}')
    
print('-'*40)       
