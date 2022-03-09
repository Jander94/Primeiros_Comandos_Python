import os
os.system('cls') or None
nota = 0
lista = []
dados = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1+nota2)/2
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    lista.append(media)
    dados.append(lista[:])
    lista.clear()
    resp = input('Quer continuar? [S/N]: ').upper()[0]
    if resp in 'N':
        break
print('-='*30)
print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":>5}')
for c in range(len(dados)):
    print(f'{c:<5}{dados[c][0]:<10}{dados[c][3]:>5.1f}')

while True:
    nota = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if nota <= len(dados)-1:
        print(f'Notas de {dados[nota][0]}: {dados[nota][1]}, {dados[nota][2]}')
        print('-='*30)
    elif nota == 999:
        print('Finalizando... \nTenha um bom dia')
        break
    else:
        print('Valor inválido')
