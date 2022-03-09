numeros = list()
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Adicionado com sucesso')
    else:
        print('Numero ja adicionado. ')
    resposta = input('Quer continuar?: ').upper()[0]

numeros.sort()
print(f'Números digitados: {numeros}')
