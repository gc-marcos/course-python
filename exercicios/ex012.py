preco = float(input('Digite o valor do produto: R$ '))
desc = preco - (preco * 5 / 100)
print('O valor com desconto é R$ {:.2f}'.format(preco*0.95))
print('O valor com desconto é R$ {:.2f}'.format(desc))
