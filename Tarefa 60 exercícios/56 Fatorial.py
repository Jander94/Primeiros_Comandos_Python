n = int(input('Digite um número: '))
print(f'{n}! = ',end=' ')
f = 1
while n >= 1:
    print(n, end=' ')
    if n > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    f *= n
    n -= 1
print(f)
