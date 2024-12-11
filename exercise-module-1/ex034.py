'''sal = float(input('Seu salário atual é R$ '))
va = (sal / 100) * 115 if sal <= 1000 else (sal / 100) * 110
print('Seu salário atual será de R$ {}'.format(va))'''

sal = float(input('Valor do seu salário é R$ '))
if sal <=1250:
    va = sal + (sal * 15 / 100)
else:
    va = sal + (sal * 10 / 100)
print('Salario antes do aumento R$ {:.2f} e depois do aumento R$ {:.2f}'.format(sal, va))
