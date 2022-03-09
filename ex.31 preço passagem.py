d = int(input('Qual a distância da viagem: '))
if d <= 200:
    print('Preço da passagem é R${:.2f}'.format(d*0.50))
else:
    print('Preço da passagem R${:.2f}'.format(d*0.45))

