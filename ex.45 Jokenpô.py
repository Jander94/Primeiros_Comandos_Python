from random import randint
from time import sleep
print('\033[1;31m='*10)
print(' Jokenpô')
print('==========\033[m')
jogo = ('Pedra', 'Papel', 'Tesoura')
j1 = randint(0, 2)
print('''\033[1;32mSuas opções:
[0] Pedra
[1] Papel
[2] Tesoura\033[m''')
j2 = int(input('\033[1;31mQual sua Jogada: \033[m'))
print('\033[1;33mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ\033[m')
print('\033[1;34m='*29)
print('Computador escolheu {}'.format(jogo[j1]))
print('Você escolheu {}'.format(jogo[j2]))
print('='*29,'\033[1;31m')
if j1 == 0: #Computador jogou Pedra
    if j2 == 0:
        print('\033[1;36mEMPATE')
    elif j2 ==1:
        print('\033[1;36mVocê venceu')
    elif j2 ==2:
        print('\033[1;36mVocê perdeu haha')
    else:
        print('\033[1;36mJogada Inválida!')
elif j1 == 1: #Computador jogou papel
    if j2 == 0:
        print('\033[1;36mVocê perdeu haha')
    elif j2 == 1:
        print('\033[1;36mEMPATE')
    elif j2 == 2:
        print('\033[1;36mVocê venceu')
    else:
        print('\033[1;36mJogada Inválida!')

elif j1 == 2: #computador jogou tesoura
    if j2 == 0:
        print('\033[1;36mVocê venceu')
    elif j2 == 1:
        print('\033[1;36mVocê perdeu haha')
    elif j2 == 2:
        print('\033[1;36mEMPATE')
    else:
        print('\033[1;36mJogada Inválida!')

