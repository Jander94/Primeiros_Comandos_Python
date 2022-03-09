from random import randint
j1 = randint(0,10)
print('')
print('Vou pensar em um número de 0 a 10 tente adivinhar')
print('')
j2 = int(input('Em que número pensei: '))
tentativas = 0
while j2 != j1:
    if j2 > j1:
        j2 = int(input('Menos... tente novamente: '))
    else:
        j2 = int(input('Mais... tente novamente: '))
    tentativas += 1
print(f'VOCÊ ACERTOU!!! O NÚMERO É {j2}. \nVOCÊ TENTOU {tentativas+1} VEZES.')
