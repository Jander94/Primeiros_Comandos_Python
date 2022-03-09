print('')
senha = int(input('Qual sua senha: '))
print('')
t = 0
while t != senha:
    t=int(input('Digite a senha novamente: '))
    print('')
    if t != senha: 
        print('Senha incorreta. Tente novamente')
        print('')
print('Senha confirmada com sucesso!')
print('')
