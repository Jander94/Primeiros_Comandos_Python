n1 = int(input('Digite um número: '))
n2= int(input('Digite outro número: '))
menu = 0
while menu != 5:
    menu = int(input('''Qual operação deseja:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR O PROGRAMA \n'''))
    if menu == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif menu == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
        else:
            print(f'O maior número entre {n1} e {n2} é {n2}')
    elif menu == 4:
        print('Digite os valores novamente: ')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
print('''FINALIZANDO...
Até a próxima...''')
