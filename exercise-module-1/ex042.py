print('Vamos saber de que tipo é seu triangulo!')
ld1 = float(input('Digigite primeiro segmento: '))
ld2 = float(input('Digite o segundo segmento: '))
ld3 = float(input('Digite o terceiro segmento: '))

if ld1 < ld2 + ld3 and ld2 < ld1 + ld3 and ld3 < ld1 +ld2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if ld1 == ld2 == ld3:
        print('Equilátero')
    elif ld1 != ld2 != ld3 != ld1:
        print('Escaleso')
    else:
        print('Isósceles')
else: 
    print('Os segmentos acima não podem formar um triângulo!')    