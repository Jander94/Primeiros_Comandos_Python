resp = 'S'
soma = cont = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while resp not in 'SsNn':
        resp = str(input('''\033[31mresposta inválida.\033[m
        Quer coninuar?: '''))
print('\033[33mForam digitados {} números'.format(cont))
print('\033[34mA media foi de {:.2f}'.format(soma/cont))
print('\033[33mO maior nº foi {} e o menor foi {}\033[m'.format(maior, menor))
