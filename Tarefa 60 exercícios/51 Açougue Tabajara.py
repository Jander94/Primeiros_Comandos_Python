carne = int(input('''Escolha a carne: 
[1] Filé Duplo
[2] Alcatra
[3] Picanha\n'''))
qtd = float(input('Quantos kg: '))
desconto = 0
                                #Quantidade <= 5 KG
if carne == 1 and qtd <= 5:
    file = 4.9
    tipo = 'Filé Duplo'
    valor = file * qtd
elif carne == 2 and qtd <= 5:
    alcatra = 5.9
    tipo = 'Alcatra'
    valor = alcatra * qtd
elif carne == 3 and qtd <= 5:
    picanha = 6.9
    tipo = 'Picanha'
    valor = picanha * qtd
                                #Quantidade > 5KG
elif carne == 1 and qtd > 5:
    file = 5.8
    tipo = 'Filé Duplo'
    valor = file * qtd
elif carne == 2 and qtd > 5:
    alcatra = 6.8
    tipo = 'Alcatra'
    valor = alcatra * qtd
elif carne == 3 and qtd > 5:
    picanha = 7.8
    tipo = 'Picanha'
    valor = picanha * qtd

# pagamento no cartão, coloquei o valor 5 apenas para imprimir na NF
pagamento = input('Pagamento é no cartão Tabajara?: ').upper()[0]
if pagamento == 'S':
    desconto = 5

print(f'{"Nota Fiscal":^30}')
print(f'{tipo:.<20} ({qtd:.2f}Kg)',end='  ')
print(f'R$ {valor:.2f}')
print(f'{"Cartão Tabajara":.<30}',end='  ')
print(pagamento)
print(f'{"Desconto":.<24} ({desconto}%)', end='  ')
                                        #calcula valor com desconto
if pagamento == 'S':
    total = valor - (valor * 0.05)
    print(f'R$ {valor*0.05:.2f}')
else:
    total = valor
    print(f'R$ {0.00}')
print(f'{"Total":.<29}',end='  ')
print(f'R$ {total:.2f}')
