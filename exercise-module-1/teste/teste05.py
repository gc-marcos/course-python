nome = str(input('Digite seu nome: '))
if nome == 'Marcos':
    print('Marcos é lindo!!')
else:
    print('Seu nome é tão comum!!')
print('Olá! {}.'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua nota final foi {:.1f}'.format(m))
if m >= 6.0:
    print('Vocế está de parabéns!!')
else:
    print('Você tem que estudar mais!!')

m1 = float(input('Digite um numero: '))
m2 = float(input('Digite mais um numero: '))
d = (m1 + m2)/2
print('Parabéns!' if d >= 6 else 'Estude mais!!')
