from random import randint
num = (randint(0,20),randint(0,20),randint(0,20),randint(0,20),randint(0,20),)
print('Os nnúmeros foram: ')
for n in num:
    print(n, end=' ')
print(f'\nO maior é {max(num)}')
print(f'O menor é {min(num)}')
