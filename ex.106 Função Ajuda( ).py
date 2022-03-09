import os
os.system('cls') or None
from time import sleep

c = ('\033[m',          # 0 - sem cores
     '\033[41m',        # 1 - Vermelho
     '\033[1;31;42m',   # 2 - Verde
     '\033[30;43m',     # 3 - amarelo
     '\033[44m',        # 4 - azul
     '\033[45m',        # 5 - roxo
     '\033[1;30;46m'    # 6 
)

def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[cor], end='')
    print('*'*tam)
    print(f'  {msg}')
    print('*'*tam)
    print(c[0], end='')
    

def ajuda(comando):
    titulo(f'Acessando o manual do comando {comando}', 2)
    sleep(2)
    print(c[4], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = input('Função ou Biblioteca >>> ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        
titulo('VOLTE SEMPRE...', 3)
