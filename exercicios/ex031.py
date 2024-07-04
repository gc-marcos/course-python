'''dis = int(input('Qual é a distancia da sua viagem? '))
vl = 0.50
if dis <= 200:
    print('O valor da viagem é {:.2f}'.format(dis * vl))
else:
    print('O valor da viagem é {:.2f}'.format(dis * 0.45))'''

dis = float(input('Qual é a distancia de sua viajem? '))
print('Sua viajem tem {}Km.'.format(dis))

'''if dis <= 200:
    vl = dis * 0.50
else:
    vl = dis * 0.45'''

vl = dis * 0.50 if dis <= 200 else dis * 0.45

print('O preço de sua viajem será de R$ {:.2f}.'.format(vl))
