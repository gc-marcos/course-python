'''n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
print('Numero menor é {}.'.format(min(n1, n2, n3)))
print('Numero maior é {}.'.format(max(n1, n2, n3)))'''

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior =  b
if c > a and c > b:
    maior = c
print('O numero menor é {}'.format(menor))
print('O numuro maior é {}'.format(maior))
