import os
os.system('cls')or None

def area(l, c):
    print(f'A área do terreno {l}x{c} é {l*c}m²')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)

