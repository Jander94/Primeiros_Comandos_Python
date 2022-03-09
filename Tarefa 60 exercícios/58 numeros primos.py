n = int(input('Digite um número: '))
teste = [1,2,3,4,5,6,7,8,9,10]
cont = 0
for t in teste:
    if n % t == 0:
        cont += 1

if cont > 2:
    print(f'O nº {n} não é primo. \nDe 1 a 10 ele foi divisível {cont} vezes.')        

else:
    print(f'O nº {n} é Primo. Ele é divisível apenas por 1 e por {n}')
