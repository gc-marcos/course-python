nome = str(input('Digite uma frase: ')).upper().strip()
print('A primeira letra A apareceu {} vezes na frase.'.format(nome.count('A')))
print('Em que posição ela apareceu a primeira vez? {}'.format(nome.find('A')+1))
print('Em que posição ela aparece a última vez? {}'.format(nome.rfind('A')+1))
