altura = float(input('Digite sua altura: '))
pesoatual = float(input('Digite seu peso: '))
sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MF':
    print('\033[31;1mSexo inválido.\033[m')
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
if sexo in 'M':
    peso = (72.7*altura) - 58
    if pesoatual > peso:
        print('Você está acima do peso.')
    if pesoatual < peso:
        print('Você esta abaixo do peso.')
    if pesoatual == peso:
        print('Você está com o peso ideal')
    print(f'Seu peso ideal é {peso:.2f} (Sexo Masculino)')    
else:
    peso = (62.1*altura) - 44.7
    if pesoatual > peso:
        print('Você está acima do peso.')
    if pesoatual < peso:
        print('Você esta abaixo do peso.')
    if pesoatual == peso:
        print('Você está com o peso ideal')
    print(f'Seu peso ideal é {peso:.2f} (Sexo Feminino)')