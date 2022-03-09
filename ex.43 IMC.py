p = float(input('Qual seu peso: '))
a = float(input('Qual sua altura: '))
i = p / (a ** 2)
if i < 18.5:
    print('Seu IMC está em {:.2f} \nVocê está abaixo do peso'.format(i))
elif 18.5 <= i <= 24.9:
    print('Seu IMC está em {:.2f}\nVocê está com o peso Ideal'.format(i))
elif 25 <= i <= 29.9:
    print('Seu IMC está em {:.2f}\nVocê está com Sobrepeso'.format(i))
elif 30 <= i <= 34.9:
    print('Seu IMC está em {:.2f}\nVocê está com Obesidade grau I'.format(i))
elif 35 <= i <= 39.9:
    print('Seu IMC está em {:.2f}\nVocê está com Obesidade grau II'.format(i))
else: #i >= 40:
    print('Seu IMC está em {:.2f}\nVocê está com Obesidade Grau III ou Mórbida'.format(i))
