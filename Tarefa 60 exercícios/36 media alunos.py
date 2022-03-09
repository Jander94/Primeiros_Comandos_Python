n1 =  float(input('1ª Nota: '))
n2 =  float(input('2ª Nota: '))
media = (n1+n2)/2
if 9 < media <= 10:
    nota = 'A'
if 7.5 < media <= 9:
    nota = 'B'
if 6 < media <= 7.5:
    nota = 'C'
if 4 < media <= 6:
    nota = 'D'
if 0 < media <= 4:
    nota = 'E'
print(f'A média foi {media} Nota: {nota}')
