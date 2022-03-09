num = int(input('Digite um número menor que 1000: '))
while num > 1000:
    print('Numero digitado maior que 1000.')
    num = int(input('Digite um número menor que 1000: '))
centena = num // 100
dezena = num // 10 % 10
unidade = num // 1 % 10
print(f'O número {num} tem: \n{centena} centenas \n{dezena} dezenas \n{unidade} unidades')

