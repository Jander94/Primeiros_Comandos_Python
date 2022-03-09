dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if mes==1 or mes==3 or mes== 5 or mes==7 or mes==8 or mes==10 or mes==12:
    if 1 <= dia <= 31 and 0 < ano < 9999:
        data = 'valida'
    else:
        data = 'invalida'
elif mes==4 or mes==6 or mes==9 or mes==11:
    if 1 <= dia <=30 and 0 < ano < 9999:
        data = 'valida'
    else:
        data = 'invalida'
elif mes == 2:
    if ano%4==0 or ano%400==0 and ano%100!=0:
        if 1 <= dia <=29:
            data = 'valida'
        else:
            data = 'invalida'
    else:
        if 1 <= dia <= 28:
            data = 'valida'
        else:
            data = 'invalida'

if data == 'valida':
    print(f'A data {dia}/{mes}/{ano} é Válida')
else:
    print(f'A data {dia}/{mes}/{ano} é Inválida')

