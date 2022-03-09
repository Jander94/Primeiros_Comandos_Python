from matematica import limpar
limpar()

def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))  
        except(ValueError, TypeError):
            print('\033[1;31mERRO. Digite um número inteiro válido.\033[m')
            continue
        return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except(ValueError, TypeError):
            print('\033[1;31mERRO. Digite um número Real válido.\033[m')
            continue
        return num


n = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor Real: ')
print(f'''Inteiro: {n}
Real: {n2}''')

