nomevelho = ''
idadevelho = 0
menos20 = 0
mediaidade = 0
for c in range(1,5):
    print(f'-------{c}ª Pessoa------')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    mediaidade += idade
    if c == 1 and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        menos20 += 1
print(f'A média das idades é {mediaidade/4}')
print(f'{menos20} mulheres tem menos de 20 anos.')
print(f'{nomevelho} é o homem mais velho, ele tem {idadevelho} anos.')
