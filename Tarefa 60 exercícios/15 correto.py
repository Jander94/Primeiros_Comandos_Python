
altura = float(input('Qual sua altura: '))
peso = float(input('Qual seu peso: '))
imc = peso / altura**2
if imc < 18.5:
    print(f'Seu IMC deu {imc:.2f}\nVocê está abaixo do peso.')
if 18.5 < imc < 24.9:
    print(f'Seu IMC deu {imc:.2f}\nVocê esta com o peso normal.')
if 25 < imc < 29.9:
    print(f'Seu IMC deu {imc:.2f}\nVocê esta com sobrepeso.')
if 30 < imc < 34.9:
    print(f'Seu IMC deu {imc:.2f}\nVocê esta com obesidade Grau I.')
if 35 < imc < 39.9:
    print(f'Seu IMC deu {imc:.2f}\nVocê esta com obesidade Grau II.')
if imc >= 40:
    print(f'Seu IMC deu {imc:.2f}\nVocê esta com obesidade Grau III ou Mórbida.')

