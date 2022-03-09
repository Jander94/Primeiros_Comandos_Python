area = float(input('Tamanho da área a ser pintada em m²: '))
quantidade = area / 3   #Quantidade de tinta a ser utilizada
valor = 80
if quantidade <= 18:
    print(f'Serão necessários {quantidade:.2f} litros de tinta para pintar esta área.')
    print('Você deverá comprar 1 lata de tinta')
    print('Valor: R$80,00')
if quantidade > 18:
    quant = (quantidade//18)+1
    print(f'Serão necessários {quantidade:.2f} litros de tinta para pintar esta área.')
    print(f'Você deverá comprar {quant} latas de tinta')
    print(f'Valor R${80 * quant:.2f}')
    