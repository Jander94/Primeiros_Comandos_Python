from random import randint
from time import sleep
j1 = randint(0,5)   #computador sorteia um número
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...haha')
print('-=-'*20)
j2 = int(input('Em que número pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if j2 == j1:
    print('PARABÉNS VOCÊ ME VENCEU!!!')
else:
    print('Você perdeu! kkk Eu pensei no número {}'.format(j1))

