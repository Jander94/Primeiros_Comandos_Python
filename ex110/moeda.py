def limpar():
    import os
    os.system('cls') or None
    

def aumentar(preço=0, taxa=0, format=False):
    res = preço + (preço * (taxa/100))
    return res if format is False else moeda(res)


def diminuir(preço=0, taxa=0, format=False):
    res = preço - (preço * (taxa/100))
    return res if format is False else moeda(res)


def dobro(preço=0, format=False):
    res = preço*2
    return res if not format else moeda(res)


def metade(preço=0, format=False):
    res = preço/2
    return res if not format else moeda(res)


def moeda(preço=0, moeda="R$"):
    return f'{moeda} {preço:.2f}'.replace(".", ",")


def linha(tam):
    print('-'*tam)

def resumo(preço=0, aumento=0, redução=0):
    linha(30)
    print('RESUMO DO VALOR'.center(30))
    linha(30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(preço, redução, True)}')
    linha(30)
