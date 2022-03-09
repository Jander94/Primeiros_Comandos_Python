hora = float(input('Quanto você ganha por hora: R$'))
mes = int(input('Quantas horas trabalha por mês: '))
salariobruto = hora*mes
irrf = 0.11 * salariobruto
inss = 0.08 * salariobruto
sindicato = 0.05 * salariobruto
salarioliquido = salariobruto - irrf - inss - sindicato
print(f'Salário bruto: R${salariobruto:.2f}')
print(f'Valor IRRF: R${irrf:.2f}')
print(f'Valor INSS: R${inss:.2f}')
print(f'Valor Sindicato: R${sindicato:.2f}')
print(f'Salário Líquido: R${salarioliquido:.2f}')
