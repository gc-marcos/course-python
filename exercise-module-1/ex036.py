casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))
prest = anos * 12
valor_pres = casa / prest
if valor_pres <= salario * 30 / 100:
    print('Sua prestação será de R$ {:.2f} e foi Aprovado sua compra.'.format(valor_pres))
else:
    print('O valor da sua prestação é de R$ {:.2f} e ultrapassou 30% do valor de seu salario'.format(valor_pres))
