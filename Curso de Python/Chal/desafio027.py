n = str(input('Nome Completo: ')).strip()
nome =n.title().split()
print('Muito prazer em te connhecer! ')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

