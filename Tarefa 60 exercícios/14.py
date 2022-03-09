altura = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MF':
    print('\033[31;1mSexo inválido.\033[m')
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
if sexo in 'M':
    peso = (72.7*altura) - 58
    print(f'Seu peso ideal é {peso:.2f} (Sexo Masculino)')
else:
    peso = (62.1*altura) - 44.7
    print(f'Seu peso ideal é {peso:.2f} (Sexo Feminino)')
