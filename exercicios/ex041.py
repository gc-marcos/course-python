from datetime import date
data =  date.today().year
nasc = int(input('Digite o ano de nascimento: '))
div = data - nasc
print(f'Você tem {div} e sua classificação: ')
if div <= 9:
    print('MIRIM')
elif div > 9 and div <= 14:
    print('INFANTIL')
elif div <= 19:
    print('JUNIOR')
elif div <= 25:
    print('SENIOR')
else:
    print('MASTER')
    