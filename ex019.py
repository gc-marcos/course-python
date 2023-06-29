'''import random
al1 = str(input('Primeiro nome: '))
al2 = str(input('Segundo nome: '))
al3 = str(input('Terceiro nome: '))
al4 = str(input('Quarto nome: '))
al5 = str(input('Quinto nome: '))
lista = [al1, al2, al3, al4, al5]
escolhido = random.choice(lista)
print('O escolhido foi {}.'.format(escolhido))'''
from random import choice
al1 = str(input('Primeiro nome: '))
al2 = str(input('segundo nome: '))
al3 = str(input('Terceiro nome: '))
lista = [al1, al2, al3]
escolhido = choice(lista)
print('O escolhido foi {}.'.format(escolhido))

