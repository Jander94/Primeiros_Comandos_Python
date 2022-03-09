r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Os seguimentos formam um triangulo ',end=(""))
    if r1 == r2 == r3:
        print('Equilátero. Todos os lados iguais.')
    elif r1 != r2 != r3 != r1:
        print('Escaleno. Todos os lados são diferentes.')
    else:
        print('Isósceles. Dois lados iguais')
else:
    print('Os seguimentos não formam um triângulo.')
