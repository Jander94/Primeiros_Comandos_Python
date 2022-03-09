import os
os.system('cls')or None

resp = 'S'
pessoa = dict()
lista = []
idades = 0
        #Laço para cadastrar várias pessoas. Com validação para sexo e resposta de continuidade
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    idades += pessoa['idade']
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO. Digite apenas M ou F.')
    lista.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Digite apenas S ou N.')
    if resp == 'N':
        break
            #Criei variavel 'idades' para soma-las e calcular a média
media = idades / len(lista)
print('=-'*30)
print(f'A) Foram cadastradas {len(lista)} pessoas')
print(f'B) A Média de idades foi: {media:.2f}')
print('C) As mulheres cadastradas foram: ',end=' ')
            #Laço para imprimir as mulheres da lista
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='..')
print('\nD) Pessoas com idade acima da média: ', end=' ')
            #Laço para imprimir as pessoas com idade acima da média
for p in lista:
    if p['idade'] > media:
        print(f'{p["nome"]}',end='..')
