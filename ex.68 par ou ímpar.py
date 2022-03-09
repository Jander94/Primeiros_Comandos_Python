from random import randint
cont = 0
while True:
    j = int(input('Digite um número: '))
    c = randint(1, 10)
    soma = j + c
    resp = input('Par ou Ímpar [P/I]: ').strip().upper()[0]
    while resp not in 'PI':
        resp = input('Par ou Ímpar [P/I]: ').strip().upper()[0]
    print('='*30)
    print('DEU PAR' if soma % 2 == 0 else'DEU ÍMPAR')
    if resp == 'P' and soma % 2 == 0:
        cont += 1
        print('Você venceu')
        print(f'Vc jogou {j} e o computador {c} a soma é {soma}')
        print('='*30)
    elif resp == 'I' and soma % 2 != 0:
        cont += 1
        print('Você venceu')
        print(f'Vc jogou {j} e o computador {c} a soma é {soma}')
        print('='*30)
    else:
        print('Você perdeu!')
        print(f'Vc jogou {j} e o computador {c} a soma é {soma}')
        print('='*30)
        break
print(f'Você venceu {cont} vezes.')
print('='*30)


