import os
os.system('cls') or None
from datetime import datetime

dados = {'Nome': input('Nome: '),
'Nascimento': int(input('Ano de Nascimento: ')),}
dados['Idade'] = datetime.now().year - dados['Nascimento']
dados['CTPS'] = int(input('Nº CTPS [0 não tem]: '))

if dados['CTPS'] != 0:
    dados['Contrataçao'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = (dados['Contrataçao']+35)-dados['Nascimento']

print('\033[1;36m=== DADOS CTPS ===')
for c, v in dados.items():
    print(f'\033[34m{c}: {v}')
