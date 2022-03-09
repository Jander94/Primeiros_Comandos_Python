import os
os.system('cls')or None

def escreva(msg):
    tam = len(msg) + 4
    print('*' * tam)
    print(f'  {msg}')
    print('*' * tam)


escreva('Bom dia')
