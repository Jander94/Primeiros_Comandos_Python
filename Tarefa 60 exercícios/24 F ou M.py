letra = input('Digite [M] para masculino ou [F] para feminino: ').upper()
if letra != 'F' and letra != 'M':
    print('Sexo inválido')
if letra == 'F':
    print('Sexo feminino.')
if letra == 'M':
    print('Sexo masculino')
