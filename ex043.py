nome = str(input('Qual seu nome? '))
print(f'Olá, {nome}, vamos calcular seu IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print(f'{nome} seu IMC é {imc:.1f}')
if imc < 18.5:
    print(f'{nome} seu peso está abaixo!')
elif 18.5 <= imc < 25.0:
    print(f'{nome} seu peso está ideal!')
elif 25.0 <= imc < 30.0:
    print(f'{nome} seu peso está levemente acima.')
elif 30.0 <= imc < 35.0:
    print(f'{nome} seu peso está no grau 1 de obesidade.')
elif 35.0 <= imc < 40.0:
    print(f'{nome} seu peso está no grau 2 de obesidade. (SEVERA)')
else:
    print(f'{nome}seu peso está no grau 3 de obesidade. (MÓRBIDA)')



