import os
os.system('cls') or None
from random import randint
from time import sleep


def sortear(lista):
    print('Sorteando 5 valores: ',end=' ')
    sleep(2)
    for c in range(5):
        num = randint(1, 10)
        print(num, end=' ')
        sleep(0.5)
        lista.append(num)
    
   
def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    sleep(2)        
    print(f'\nA soma dos Pares é: {soma}.')

numeros = list()
sortear(numeros)
somapar(numeros)
