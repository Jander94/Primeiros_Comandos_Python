salário = float(input('Salário: R$'))
if salário <= 280:
    print(f'Salário antes do reajuste: R${salário}')
    print('Percentual de aumento: 20%')
    print(f'Valor do aumento: R${salário*0.20:.2f}')
    salário = salário + (salário*0.2)
    print(f'Salário com aumento: R$ {salário:.2f}')

if 280 < salário <= 700:
    print(f'Salário antes do reajuste: R${salário}')
    print('Percentual de aumento: 15%')
    print(f'Valor do aumento: R${salário*0.15:.2f}')
    salário = salário + (salário*0.15)
    print(f'Salário com aumento: R$ {salário:.2f}')

if 700 < salário <= 1500:
    print(f'Salário antes do reajuste: R${salário}')
    print('Percentual de aumento: 10%')
    print(f'Valor do aumento: R${salário*0.1:.2f}')
    salário = salário + (salário*0.1)
    print(f'Salário com aumento: R$ {salário:.2f}')
    
if salário > 1500:
    print(f'Salário antes do reajuste: R${salário}')
    print('Percentual de aumento: 5%')
    print(f'Valor do aumento: R${salário*0.05:.2f}')
    salário = salário + (salário*0.05)
    print(f'Salário com aumento: R$ {salário:.2f}')
