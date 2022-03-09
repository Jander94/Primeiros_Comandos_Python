n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
opcao = int(input('''Digite a opção desejada: 
[1] Par ou ímpar 
[2] Positivo ou negativo  
[3] inteiro ou decimal'''))
if opcao == 1:
    if n1 % 2 == 0:
        print(f'{n1} é par')
    else:
        print(f'{n1} é ímpar')
    if n2 % 2 == 0:
        print(f'{n2} é par')
    else:
        print(f'{n2} é ímpar')
if opcao == 2:
    if n1 < 0:
        print(f'{n1} é negativo')
    else:
        print(f'{n1} é positivo ')
    if n2 < 0:
        print(f'{n2} é negativo')
    else:
        print(f'{n2} é positivo ')
if opcao == 3:
    if n1 //1 == n1:
        print(f'{n1} é inteiro')
    else:
        print(f'{n1} é decimal')
    if n2 //1 == n2:
        print(f'{n2} é inteiro')
    else:
        print(f'{n2} é decimal')
        
