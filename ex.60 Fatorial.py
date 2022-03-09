n = int(input('Digite um número paraver seu fatorial: '))
print(f'{n}! = ', end=' ')
f = 1
while n >= 1:
    f *= n
    print(n, end=' ')
    print('x' if n > 1 else '=', end=' ')
    n -= 1
print(f)
