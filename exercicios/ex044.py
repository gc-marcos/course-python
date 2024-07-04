print('{:=^40}'.format(' LOJAS MARCOS '))
preco = float(input('Preço das Compras: R$ '))
print('{: ^40}'.format(' FORMA DE PAGAMENTO ')) #Para fazer o menu pode ser assim (''' .... ''')
print('[ 1 ] à vista dinheiro / cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2X no cartão')
print('[ 4 ] 3X ou mais no cartão')
op = int(input('Qual é sua opção? '))
"""
if op == 1:
    op1 =  (preco / 100) * 90
    print(f'Sua compra é de R$ {preco:.2f} e vai custar R$ {op1:.2f} no final.')
elif op == 2:
    op2 = (preco / 100) * 95
    print(f'Sua compra é de R$ {preco:.2f} e vai custar R$ {op2:.2f} no final.')
elif op == 3:
    print(f'Sua compra será o preço normal R$ {preco:.2f}.')
elif op == 4:
    op4 = (preco / 100) * 120
    print(f'Sua compra é de R$ {preco:.2f} e vai custar R$ {op4:.2f} no final.')"""
if op == 1:
    total = preco - (preco * 10 / 100)
elif op == 2:
    total = preco - (preco * 5 / 100)
elif op == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2X de R$ {parcela:.2f}. SEM JUROS')
elif op == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc:.2f} de R$ {parcela:.2f}. COM JUROS')
else:
    total = preco
    print(f'OPÇÃO INVALIDA!!')
print(f'Sua compra será de R$ {preco:.2f} e vai custar R$ {total:.2f}.')
