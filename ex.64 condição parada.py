'''n = int(input(('Digite um número: ')))
cont = 0
soma = n
while n != 999:
    n = int(input('Digite outro número: '))
    cont += 1
    soma += n
print('FIM')
print(f'Foram digitados {cont} números \nA soma deles é {soma - 999}')'''

#Colocando comando (n) no final da repetição
#assim que digitar o flag, a repetição encerra antes de soma-lo

n = int(input(('Digite um número: ')))
cont = 0
soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite outro número: '))
print('FIM')
print(f'Foram digitados {cont} números \nA soma deles é {soma}')
