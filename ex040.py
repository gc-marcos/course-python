nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota do {}: '.format(nome)))
n2 = float(input('Digite a segunda nota do {}: '.format(nome)))
media = (n1 + n2)/2
print('A média de {} é {}'.format(nome, media))
if media < 5.0:
    print('{} está REPROVADO!'.format(nome))
elif 5.0 <= media <= 6.9:
    print('{} está de RECUPERAÇÃO!'.format(nome))
else:
    print('{} está APROVADO!'.format(nome))