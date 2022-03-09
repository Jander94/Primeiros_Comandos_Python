from math import sin,cos,tan,radians
a = float(input('Digite o angulo: '))
seno = sin(radians(a))
coseno = cos(radians(a))
tangente = tan(radians(a))
print('O angulo {} tem o seno {:.2f} o coseno {:.2f} tangente {:.2f}'.format(a,seno,coseno,tangente))
