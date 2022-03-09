l1 = int(input('Primeira reta: '))
l2 = int(input('Segunda reta: '))
l3 = int(input('Terceira reta: '))
if (l1 + l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:
    print('Os seguimentos formam um triângulo: ',end=' ')
    if l1 == l2 == l3:
        print('EQUILÁTERO') 
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos não podem formar um triângulo')
