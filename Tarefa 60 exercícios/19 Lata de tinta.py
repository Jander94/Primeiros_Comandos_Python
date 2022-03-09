area = float(input('Tamanho da área a ser pintada em m²: '))
quantidade = area / 6   #Quantidade de tinta a ser utilizada
lata = 18
cont = 0
while quantidade > lata:
    cont+= 1
    lata += 18
q1 = (quantidade//18)+1   #Quantidade lata 18L
q2 = (quantidade//3.6)+1   #Quantidade lata 3,6L
q3 =  quantidade - cont*18  #Quantidade tinta total - quantidade inteira lata 18L necessária
q4 = (q3 // 3.6)+1           #O que passar da lata de 18L interar com a de 3,6L
print(f'Serão necessários {quantidade:.2f} litros de tinta para pintar esta área.')
print(f'Você poderá comprar: {q1} latas de tinta de 18L valor: R$ {q1*80:.2f}')
print(f'Você poderá comprar: {q2} latas de tinta de 3,6L valor: R$ {q2*25:.2f}')
print(f'Você poderá comprar: {cont} latas de 18L + {q4} latas de 3,6L Valor: R$ {(cont*80)+(q4*25)}')
