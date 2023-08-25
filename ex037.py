num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das base de converção:
[1] Converter para Binário
[2] Converter para octal
[3] Converter para Hexadecimal''')
opc = int(input(' Sua opcção: '))
if opc == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalidade!')
