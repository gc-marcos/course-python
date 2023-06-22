dia = float(input('Quantos dias foi alugado o carro: '))
km = float(input('Quantos Km rodou com carro: '))
d =  dia * 60.00
k = km * 0.15
total = d + k
t = (dia * 60) + (km * 0.15)
print('O total a pagar é de R$ {}'.format(total))
print('Outra formula R$ {}'.format(t))