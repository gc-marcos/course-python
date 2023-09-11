num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das base de converção:
[1] Converter para Binário
[2] Converter para octal
[3] Converter para Hexadecimal''')
opc = int(input(' Sua opcção: '))
if opc == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}')
elif opc == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif opc == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção invalidade!')
