from random import randint
from time import sleep
pc =  randint(0, 5) #PC escolher o numero
print('---' * 20)
print('Vou escolher um numero entre 0 e 5. Tente adivinhar!!!')
print('---' * 20)
jog = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jog == pc:
    print('Parabéns você venceu!!')
else:
    print('Tente outra vez, você perdeu!! Eu pensei em {}'.format(pc))