pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range(pt, pt+(11-1)*r, r):
    print(c, end=' ')
