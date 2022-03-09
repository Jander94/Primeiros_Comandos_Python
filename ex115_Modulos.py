def limpar():
    import os
    os.system('cls') or None

                        ### COMANDOS PARA A INTERFACE ###
def linha(tam=42):
    print('-'*tam)


def titulo(msg):
    linha()
    print(f'{msg}'.center(42))
    linha()

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print('\033[1;31mERRO. Digite um número inteiro válido.\033[m')
            continue
        return num

def menu(lista):  #coloque dentro de uma lista o que deve aparecer no menu. menu([lista])
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista: 
        print(f'\033[35m{c} - \033[34m{item}\033[m')
        c+=1
    linha()
    opção = leiaInt('\033[36mSua Opção: \033[m')
    return opção

                            ### COMANDOS PARA O ARQUIVO ###

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler Arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao esccrever os dados')
        else:
            print(f'{nome} cadastrado com sucesso!')
            a.close()


