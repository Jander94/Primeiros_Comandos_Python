mais18 = homem = menos20 = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        mais18 += 1
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        print('\033[31mResposta incorreta.\033[m')
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    print('-'*30)
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        menos20 += 1
    resp = input('Deseja continuar [S/N]: ').strip().upper()[0]
    while resp not in 'SN':
        print('\033[31mResposta incorreta.\033[m')
        resp = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if resp == 'N':
        print('-'*30)
        break

print(f'{mais18} pessoas tem mais de 18 anos')
print(f'{homem} homens foram cadastrados')
print(f'{menos20} mulheres tem menos de 20 anos')

