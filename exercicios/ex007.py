aluno = str(input('Nome do aluno: '))
nota1 = float(input('Digite a nota do 1º sem.: '))
nota2 = float(input('Digite a nota do 2º sem.: '))
media = (nota1 + nota2)/2
print('O {} tirou na 1º nota {} e na 2º {}, sendo a média final {:-^9}. '.format(aluno, nota1, nota2, (nota1 + nota2)/2))
print('A media do {} é {}'.format(aluno, media))