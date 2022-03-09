import os
os.system('cls') or None
ficha = list()
while True:
    nome = input('Nome: ')
    nota1= float(input('1ª Nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar?: [S/N: ').upper()[0]
    if resp in 'N':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    nota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if nota == 999:
        print('Finalizando... \n<< VOLTE SEMPRE >>')
        break
    if nota <= len(ficha)-1:
        print(f'Notas de {ficha[nota][0]}: {ficha[nota][1]}')
