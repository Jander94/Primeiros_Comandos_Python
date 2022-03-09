r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32;40mOs seguimentos formam um triângulo.\033[m')
else:
    print('\033[4;31;40mOs seguimentos não formam um triângulo.\033[m')
