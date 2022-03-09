nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
media = (nota1+nota2)/2
if media >= 7:
    print('APROVADO', end=' ')
if media < 7:
    print('REPROVADO')
if media == 10:
    print('COM DISTINÇÃO!!!')
