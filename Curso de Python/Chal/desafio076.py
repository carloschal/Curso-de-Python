lista = ('Pão', 0.25,
         'Queijo', 15.00,
         'Refrigerante', 4.50,
         'Açucar', 3.0,
         'Feijão', 4.5,
         'Fubá', 1.75)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' *40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)