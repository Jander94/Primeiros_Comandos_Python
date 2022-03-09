import os
os.system('cls')or None

def notas(*n, sit=False):
    dados = dict()
    dados['total'] = len(n)
    dados['Maior'] = max(n)
    dados['Menor'] = min(n)
    dados['Média'] = float((f'{sum(n)/len(n):.1f}'))
    if sit == True:
        if dados['Média'] >= 7:
            dados['Situação'] = 'Boa'
        elif dados['Média'] >=5:
            dados['Situação'] = 'Razoável'
        else:
            dados['Situação'] = 'Ruim'
    print(dados)


notas(0,6,4,12,4,sit=True)