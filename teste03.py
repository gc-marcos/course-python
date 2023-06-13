print('Ordem de precedecia')
print('1ª () - Parentes')
print('2ª ** Exponenciação')
print('3ª * Multiplicação, / Divisão, // Divisão Inteira, % Resto da Divisão')
print('4ª + Adição, - Subtração')
nome = str(input('Qual seu nome? '))
print('Prazer em te conhecer {:_^30}!'.format(nome))
n1 = int(input('Digite um Valor: '))
n2 = int(input('Digite outro Valor: '))
s = n1 + n2
m = n1 * n2
sb = n1 - n2
dr = n1 // n2
d = n1 / n2
e = n1 ** n2
print('A soma é {} | {} | {} | {} | {} | {}.'.format(s, m, sb, dr, d, e))
print('A multiplicação é {}'.format(m))
print('A Subtração é {}'.format(sb))
print('O resto da divisão é {}'.format(dr))
print('A divisão inteira é {:.2f}'.format(d), end=' ')
print('O produto é {}'.format(e))
