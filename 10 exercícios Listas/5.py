cidades = []
repetidas = []
for c in range(8):
    cid = input('Nome da cidade: ')
    cidades.append(cid)
    qtd = cidades.count(cid)
    if qtd > 1:
        repetidas.append(cid)

cidades.insert(2,'são Paulo')
print(f'Cidades: {cidades}')
print(f'Repetidas: {repetidas}')
cidades.sort()
print(f'Cidades ordenada: {cidades}')


