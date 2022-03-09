import os
os.system('cls') or None
                #Dados nome jogador e numero de partidas
dados = {}
gol = []
dados['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
                #Usei um laço para perguntar quantos gols em cada partida
for c in range(partidas):
    gol.append(int(input(f'Quantos gols na {c+1}ª partida: ')))
dados['gols'] = gol[:]
                #Sum(gol) para somar os valores que foram digitados na LISTA gol
dados['total'] = sum(gol)
print('=-'*30)
print(dados)
print('=-'*30)
            #Usando o laço com o dados.items() para relacionar a chave com o valor
for a, b in dados.items():
    print(f'    {a} recebeu: {b}')
print('=-'*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas:')
            #Usando o laço com o enumerate(gol) para pegar o indice que esta cada valor de gol
for i, c in enumerate(gol):
    print(f'   => Na {i+1}ª partida fez {c} gols')
print(f'Foi um total de {dados["total"]} gols')
print('=-'*30)
