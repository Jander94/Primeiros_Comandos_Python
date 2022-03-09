v = float(input('Velcidade do carro: '))
if v > 80:
    print('Você foi multado. Valor da multa: R${:.2f}'.format((v-80)*7))
else:
    print('Velocidade aceitável.')
