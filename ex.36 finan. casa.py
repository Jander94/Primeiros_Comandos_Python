valor = float(input('Valor do imóvel: '))
salario = float(input('Salário mensal: '))
qtd = float(input('Quantos anos: '))
v = valor / (qtd * 12)
m = salario * (30/100)
if m < v:
    print('A parcela será de: {:.2f}, \033[31msalário incompatível\033[m.'.format(v))
else:
    print('Empréstimo aprovado!\033[32mValor da parcela R${:.2f}\033[m'.format(v))
