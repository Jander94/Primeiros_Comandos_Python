alcool = 1.90
gasolina = 2.50

#Validar a opção
combustivel = input('Alcool ou Gasolina: ').upper()[0]
while combustivel not in 'AG':
    print('OPÇÃO INVÁLIDA')
    combustivel = input('Alcool ou Gasolina: ').upper()[0]

#Se escolher Alcool
if combustivel == 'A':
    litroA = int(input('Quantos litros de alcool vai abaster: '))
    if litroA <= 20:
        alcool = alcool - (alcool * 0.03)
    elif litroA > 20:
        alcool = alcool - (alcool * 0.05)
    print(f'Valor do alcool com desconto: {alcool:.2f}')
    print(f'Valor a Pagar: R$ {alcool * litroA:.2f}')

#Se escolher Gasolina
if combustivel == 'G':
    litroG = int(input('Quantos litros de Gasolina vai abaster: '))
    if litroG <= 20:
        gasolina = gasolina - (gasolina * 0.04)
    elif litroG > 20:
        gasolina = gasolina - (gasolina * 0.06)
    print(f'Valor da gasolina com desconto: {gasolina:.2f}')
    print(f'Valor a Pagar: R$ {gasolina * litroG:.2f}')

