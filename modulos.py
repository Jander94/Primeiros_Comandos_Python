def limpar():
    '''==>> Limpa o Terminal.'''
    import os
    os.system('cls') or None

def leiaInt(txt):
    ok = False
    valor = 0
    while True:
        num = input(txt)
        if num.isnumeric():
            valor = int(num)
            ok = True         
        else:
            print('\033[1;31mERRO. Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

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

