import os
os.system('cls') or None
from time import sleep

def linha():
    print('-=' * 20)

def maior(*num):
    linha()
    print(f'Analisando os valores {num}...')
    sleep(2)
    print(f'Foram informados {len(num)}  valores')
    sleep(2)
    print(f'O maior valor foi {max(num)}')
    

maior(1,4,6,12,8,9)
