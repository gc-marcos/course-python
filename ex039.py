from datetime import date
print('''Digite o numero correspodente a seu sexo? 
[1] Masculino
[2] Feminino''')
sexo = int(input('O  numero correspodente é  '))
if sexo == 1:
    atual =  date.today().year
    nasc = int(input('digite o ano em que nasceu: '))
    idade = atual - nasc
    print('Euem nasceu no {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar imediatamente!!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))
else:
    print('Você não precisa se alistar!!')