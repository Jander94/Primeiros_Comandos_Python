hora = float(input('Valor da hora: R$ '))
qtdhora = int(input('Quantidade de horas trabalhadas: '))
saláriobruto = hora * qtdhora
inss = saláriobruto * 0.1

if saláriobruto <= 900:
    irrf = 0
if 900 < saláriobruto <= 1500:
    irrf = 5
    ir = 0.05
if 1500 < saláriobruto <= 2500:
    irrf = 10
    ir = 0.1
if saláriobruto > 2500:
    irrf = 20
    ir = 0.2
if saláriobruto > 900:
    impostorenda = ir*saláriobruto
    totaldesconto = inss+impostorenda
else:
    totaldesconto = inss
print(f'Salário Bruto:({hora}*{qtdhora})            :R$ {saláriobruto:.2f}')
if saláriobruto > 900:
    print(f'(-) IRRF ({irrf}%)                    :R$ {ir*saláriobruto:.2f}')
else:
    print(f'(-) IRRF ({irrf}%)                    :R$ 0,00')
print(f'(-) INSS (10%)                   :R$ {inss:.2f}')
print(f'FGTS (11%)                       :R$ {saláriobruto*0.11}')
print(f'Total de descontos               :R$ {totaldesconto}')
print(f'Salário Liquido:                 :R$ {saláriobruto - totaldesconto}')
