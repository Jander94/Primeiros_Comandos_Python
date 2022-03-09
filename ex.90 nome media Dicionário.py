import os
os.system('cls') or None
aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = ('Aprovado')
elif 5 < aluno['media'] < 7:
    aluno['situaçao'] = ('Recuperação')
else:
    aluno['situaçao'] = ('Reprovado')

for k, v in aluno.items():
    print(f'{k}: {v}')
