vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('MULTADO!! Utrapassou o limite de 80 Km/h.')
    multa = (vel - 80) * 7
    print('Terá que pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia!!')