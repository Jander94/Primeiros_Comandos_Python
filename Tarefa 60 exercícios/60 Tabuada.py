n = int(input('Tabuada de: '))
inicio = int(input('Inicio da tabuada: '))
fim = int(input('Fim da tabuada: '))
if fim < inicio:
    print('Valores inválidos, início menor que o fim.')
    exit()
while inicio <= fim:
    print(f'{inicio} x {n} = {inicio*n}')
    inicio += 1
