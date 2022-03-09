pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
q = int(input('Quantos termos você quer: '))
a = 1
total = 0
while q != 0:
    total += q
    while a <= total:
        print(pt, end=' ')
        pt += r
        a += 1
    q = int(input('\nQuantos termos a mais vc quer ver: '))
print(f'FIM. \nForam mostrados {total} termos.')
