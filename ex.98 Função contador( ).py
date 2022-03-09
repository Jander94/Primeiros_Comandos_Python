import os
os.system('cls')or None
from time import sleep

def linha():
    print('-=' * 20)

def contador(inicio, fim, passo):
    linha()
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contando de {inicio} ate {fim} de {passo} em {passo}:')
    sleep(2.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont -= passo
    print()
    
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem...')
i = int(input('Início: ' ))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
linha()
