nome = str(input('Qual seu nome? '))
print('Olá, {}.'.format(nome))
if nome == 'Marcos':
    print('Seu nome é bonito.')
elif nome == 'Margarete' or nome == 'Antonia':
    print('É um belo nome feminino')
elif nome in 'Matheus Junior':
    print('Seu nome é diferente!')
else:
    print('Seja bem vindo!')