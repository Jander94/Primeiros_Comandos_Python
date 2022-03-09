p = float(input('Preço doproduto: R$'))
print('Qual a condição de pagamento: ')
c = int(input('[1] Á vista - Dinheiro/cheque(10% desconto)\n[2] Á vista no cartão(5% desconto)\n[3] 2x Cartão(preço normal)\n[4] 3x ou mais no cartão(20% juros)\n'))
if c == 1:
    print('Valor a pagar: R${}'.format(p - (p * 0.1)))
elif c == 2:
    print('Valor a pagar R${}'.format(p - (p*0.05)))
elif c == 3:
    print('Valor a pagar: R${}'.format(p))
elif c == 4:
    print('Valor a pagar: R${}'.format(p+(p*0.2)))
else:
    print('Opção inválida tente novamente.')
