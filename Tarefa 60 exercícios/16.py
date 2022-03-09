regulamento = 50
peso = int(input('Digite a quantidade pescada: '))
if peso > regulamento:
    excesso = peso - regulamento
    multa = excesso * 4
    print(f'Houve excesso de {excesso}Kg \nA multa a pagar é R${multa:.2f}')
else:
    excesso = 0
    multa = 0
    print(f'Não houve excesso de peso. \nExcesso: {excesso} \nMulta: {multa}')

