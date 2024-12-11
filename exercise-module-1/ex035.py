print('\033[34m-=\033[m' * 20)
print('\033[7;31;40m Analisador de Triangulo\033[m')
print('\033[34m-=\033[m' * 20)
r1 = float(input('Primeiro numero: '))
r2 = float(input('Segundo numero: '))
r3 = float(input('Terceiro numero: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')
