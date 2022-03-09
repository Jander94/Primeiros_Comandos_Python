import os
os.system('cls') or None

somapar = soma3 = maior2 = 0
        #Declarei a matriz e solicitei os valores para substituir os zeros
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para ({l}, {c}): '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
print('*-'*30)
        #Utilizei o for para mostrar os valores da matriz
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()
print('*-'*30)
print(f'A soma dos valores pares é: {somapar}')
        #Utilizei o for para alternar na linha. A coluna é sempre a mesma
for l in range(3):
    soma3 += matriz[l][2]
print(f'A soma da 3ª coluna é: {soma3}')
        #Utilizei o for para alternar na coluna. A linha é sempre a mesma
for c in range(3):
    if matriz[1][c] > maior2:
        maior2 = matriz[2][c]

print(f'Maior valor da 2ª linha: {maior2}')
