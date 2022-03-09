palavras = ('kawasaki', 'suzuki','yamaha','honda','kasinski','huskqvarna')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos: ', end=' ')
    for i in c:
        if i.lower() in 'aeiou':
            print(i, end=' ')

