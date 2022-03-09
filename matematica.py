def limpar():
    import os
    os.system('cls') or None

def fatorial(num, show=False):
    """--> Calcula o fatorial de um número.
    num: número a ser calculado
    show: (opcional) Mostrar ou não a conta.
    """
    if show == False:
        fat = 1
        n = num
        while num >= 1:
            fat = fat*num
            num -= 1
        print(f'Fatorial de {n}: {fat}')
    else:
        print(f'{num}! = ',end='')
        fat = 1
        while num >= 1:
            fat *= num
            print(f'{num}', end=' ')
            print('x' if num > 1 else '=', end=' ')
            num -= 1
        print(fat)

def tabuada(n):
    print(f'Tabuada de {n}:')
    print('='*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('='*30)

def triangulo(r1, r2, r3):
    if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
        print('Os seguimentos formam um triangulo ',end=(""))
        if r1 == r2 == r3:
            print('Equilátero. Todos os lados iguais.')
        elif r1 != r2 != r3 != r1:
            print('Escaleno. Todos os lados são diferentes.')
        else:
            print('Isósceles. Dois lados iguais')
    else:
        print('Os seguimentos não formam um triângulo.')