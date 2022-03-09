import os
os.system('cls') or None
jogadores = []
dados = {}
gol = []
while True:
    dados.clear()
    gol.clear()
        #Solicita dados pelo teclado
    dados['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
    for c in range(partidas):
        gol.append(int(input(f'Quantos gols na {c+1}ª partida: ')))
    dados['gols'] = gol[:]
    dados['total'] = sum(gol)
    jogadores.append(dados.copy())
        #Solicita continuidade com validação
    while True:
        resp = input('quer continuar? [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Digite apenas S ou N')
    if resp == 'N':
        break
    print('-'*30)
        #Cabeçalho dos dados
print('=-'*30)
print(f'{"cod":<6}',end='')
for k in dados.keys():
    print(f'{k:<15}',end='')
print()
print('-'*70)
        #mostra os dados dos jogadores em uma tabela
for i,j in enumerate(jogadores):
    print(f'{i:<5}', end='')
    for v in j.values():
        print(f'{str(v):<16}',end='')
    print()
print('-'*70)
        #Mostra dados do jogador solicitado pelo usuário
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print('ERRO. Código inválido.')
    else:
        print(f'---Levantamento do Jogador {jogadores[busca]["nome"]}: ---')
        for i, j in enumerate(jogadores[busca]['gols']):
            print(f'    No {i+1}º jogo fez {j} gols')
    print('-'*70)
print()
print('>>> VOLTE SEMPRE <<<')