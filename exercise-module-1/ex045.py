from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(f'O computador escolheu {itens[computador]}')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 13)
print(f'Conputador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 13)
if computador == 0: # Computador jogou Pedra
    if jogador == 0:
        print('EMPATE!!')
    elif jogador == 1:
        print('JOGADOR VENCE!!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!!')
    else:
        print('JODADA INVÁLIDA!')    
    
elif computador == 1: # Computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE!!')
    elif jogador == 1:
        print('EMPATE!!')
    elif jodador == 2:
        print('JOAGADOR VENCE!!')
    else:
        print('JOGADA INVÁLIDA!!')
elif computador == 2: # Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE!!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!!')
    elif jogador == 2:
        print('EMPATE!!')
    else:
        print('JOADA INVÁLIDA!!')
    