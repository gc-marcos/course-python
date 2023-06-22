import math
from math import ceil
import random
import
num = random.randint(1, 1000)
raiz = math.sqrt(num)
print('Numero escolhido foi {}.'.format(num))
print('Arredondar de outra forma a Raiz quadrade de {} é {:.2f}.'.format(num, raiz))
print('Raiz quadrade de {} é {}.'.format(num, raiz))
print('Raiz quadrada de {} é {}.'.format(num, ceil(raiz)))
print('Raiz quadrade de {} é {}.'.format(num, math.floor(raiz)))
