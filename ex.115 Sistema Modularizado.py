from ex115_Modulos import *
from time import sleep
limpar()
arq  = 'Cadastro Pessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Mostrar Pessoas Cadastradas','Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        titulo('Pessoas Cadastradas')
        print(f'{"NOME":<30}{"IDADE"}')
        linha()
        lerArquivo(arq) 
    elif resposta == 2:
        titulo('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        titulo('SAINDO DO SISTEMA...ATÉ LOGO!!!')
        break
    else:
        print('ERRO. Digite um valor válido.')
    sleep(1.5)

