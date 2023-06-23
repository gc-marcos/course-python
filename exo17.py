'''co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é {:.2f}.'.format(hi))'''

'''import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
print('hipotenusa é {:.2f}.'.format(math.hypot(ca, co)))'''

from math import hypot
from math import ceil
co = float(input('Digite cateto oposto: '))
ca = float(input('Digite cateto adjacente: '))
print('Hipotenuza é {}.'.format(ceil(hypot(ca, co))))
