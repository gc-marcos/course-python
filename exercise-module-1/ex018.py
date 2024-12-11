'''import math
ang = float(input('Digite o angulo: '))
co = math.cos(math.radians(ang))
print('Angulo de {} tem o coseno de {:.2f}'.format(ang, co))
se = math.sin(math.radians(ang))
print('Angulo de {} tem seno de {:.2f}'.format(ang, se))
ta = math.tan(math.radians(ang))
print('O Angulo de {} tem a tangente de {:.2f}'.format(ang, ta))'''

from math import cos, sin, tan, radians
angulo = float(input('Digite o angulo: '))
coseno = cos(radians(angulo))
print('O Angulo de {} tem o coseno {:.2f}'.format(angulo, coseno))
seno = sin(radians(angulo))
print('O Angulo de {} tem o seno {:.2f}'.format(angulo, seno))
tangente = tan(radians(angulo))
print('O Angulo de {} tem a tangente {:.2f}'.format(angulo, tangente))
