resposta = 'S'
numeros = []
while resposta == 'S':
    numeros.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar?: ').upper()[0]

print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Lista Decrescente: {numeros}')
if 5 in numeros:
    print(f'O numero 5 foi digitado na posição: {numeros.index(5)}')
else:
    print('O 5 não foi digitado')
