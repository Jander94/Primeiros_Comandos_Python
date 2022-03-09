dias = ('Domingo','Segunda','Terça','Quarta','Quinta','Sexta', 'Sábado')
num = int(input('Digite um número entre 1 e 7: '))
while num < 1 or num > 7:
    print('\033[31mValor inválido\033[m')
    num = int(input('Digite um número entre 1 e 7: '))
print(f'Dia da Semana: {dias[num-1]}')
