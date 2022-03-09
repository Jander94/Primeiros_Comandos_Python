n = int(input('\033[1;36mDigite um número: '))
print('Digite a opção para conversão:')
con = int(input('1 para Binário\n2 para Octal\n3 para Hexadecimal\n\033[m'))
if con == 1:
    print('\033[32mBinário: {}'.format(bin(n)[2:]))
elif con == 2:
    print('\033[1;32mOctal: {}'.format(oct(n)[2:]))
elif con == 3:
    print('\033[1;32mHexadecimal: {}'.format(hex(n)[2:]))
else:
    print('Opção inválida. Tente Novamente')
