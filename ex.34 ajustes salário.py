s = float(input('Valor do salário: '))
if s > 1250:
    print('Salário com 10% de aumento: R${}{}{}'.format('\033[1;32m', s*0.1+s, '\033[m'))
else:
    print('Salário com 15% de aumento: R${}{}{}'.format('\033[1;35m', s*0.15+s, '\033[m'))
