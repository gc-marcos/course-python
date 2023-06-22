celsius = float(input('Digite a temperatura em Graus Celsius: '))
fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
cel = (celsius*1.8) + 32
fah = (fahrenheit-32) / 1.8
gua = 9*celsius/5+32
print('{} Celsius em Fahrenheit {:.2f}'.format(celsius, cel))
print('{} Fahrenheit em Celsius {:.2f}'.format(fahrenheit, fah))
print('Resultado da fotma do Guanabara: {}'.format(gua))
