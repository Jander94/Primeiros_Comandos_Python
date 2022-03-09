
print('='*30)
print(f'{"COLETANDO DADOS":^30}')
print('='*30)
mediasalario = cont = mediafilhos = menor150 = 0   
while True:
    salario = float(input('Valor do salário: R$'))
    if salario < 0:
        break
    if salario < 150:
        menor150 += 1
    mediasalario += salario
    cont += 1
    if cont == 1:
       maiorsalario = salario
    if salario > maiorsalario:
        maiorsalario = salario 
    filhos = int(input('Quantos filhos: '))
    mediafilhos += filhos
    print('-'*30)
print(f'A média de salário das familias é R$ {mediasalario/cont:.2f}')
print(f'A média de filhos da população é de {mediafilhos/cont:.2f}')
print(f'O maior salário digitado foi: {maiorsalario:.2f}')
if menor150 == 0:
    print('Nenhuma familia ganha menos de R$150,00')
else:
    print(f'{(menor150/cont)*100:.2f}% das familias recebem menos de 150,00')
