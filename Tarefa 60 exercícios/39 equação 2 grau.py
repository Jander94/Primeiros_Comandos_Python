from math import sqrt
print('Informe os valores da equação')
a = int(input('Valor de a: '))
if a == 0:
    print('A equação não é do segundo grau')
    exit()
b = int(input('Valor de b: '))
c = int(input('Valor de c: '))
delta = (b**2) -(4*a*c)
if delta < 0:
    print(f'Delta = {delta} ')
    print('A equação não possui raízes reais.')
    exit()
if delta == 0:
    print('Delta = 0. A equação possui apenas uma raiz real')
    raiz = (-b + sqrt(delta))/2*a
    print(f'A Raiz é: {raiz}')
if delta > 0:
    print(f'Delta = {delta}. A equação possui 2 raizes reais')
    raiz1 = (-b + sqrt(delta))/(2*a)
    raiz2 = (-b - sqrt(delta))/(2*a)
    print(f'As raízes são {raiz1} e {raiz2}')

