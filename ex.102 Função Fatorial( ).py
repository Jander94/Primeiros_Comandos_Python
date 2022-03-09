import os
os.system('cls')or None

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


resp = fatorial(7, True)

