import os
os.system('cls') or None

print('-'*30)
print(f'{"JOGA NA MEGA":^30}')
print('-'*30)

from random import randint
from time import sleep

lista = []
jogos = []
qtd = int(input('Quantos jogos quer fazer?: '))
print('-='*5, f'Sorteando {qtd} Jogos','-='*5 )
tot = 1
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            
        if cont == 6:
            lista.sort()
            jogos.append(lista[:])
            lista.clear()
            break
    tot += 1

for c in range(qtd):
    sleep(0.5)
    print(f'{c+1}º Jogo: {jogos[c]}')
    sleep(1)
print('-='*5, 'Boa sorte!', '-='*5)
