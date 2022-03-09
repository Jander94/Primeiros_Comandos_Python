import os
os.system('cls')or None


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 18 <= idade < 60:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif 16 <= idade < 18 or idade >= 60:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO NEGADO.')

nas = int(input('Em que ano você nasceu: '))
voto(nas)
