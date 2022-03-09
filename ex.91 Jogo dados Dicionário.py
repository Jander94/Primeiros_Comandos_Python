import os
os.system('cls') or None
        #importar bibliotecas necessárias
from random import randint
import time
from operator import itemgetter
        #Definir valores de cada dado/jogador
print('-='*10, 'JOGO DADOS', '=-'*10)
time.sleep(1)
ranking = []
jogo = {'Jogador_1': randint(1, 6),
'Jogador_2': randint(1, 6),
'Jogador_3': randint(1, 6),
'Jogador_4': randint(1, 6)
}
        #Imprimir os valores de cada dado/jogador
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    time.sleep(1)
        #Criei uma lista para colocar os dados em ordem
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-='*23)
print(f'{"RANKING DOS JOGADORES":^40}')
print('-='*23)
time.sleep(1)
        #Imprimir na tela a colocação dos jogadores, onde 'i' = indice e 'v' = valor dentro do indice
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    time.sleep(1)
