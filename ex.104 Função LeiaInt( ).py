import os
os.system('cls')or None

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


n = leiaInt('Digite um valor: ')
print(f'Valor digitado: {n}')
