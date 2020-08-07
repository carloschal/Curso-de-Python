n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O Maior valor é {}.'.format(n1))
elif n2 > n1:
    print('O Maior valor é {}.'.format(n2))
else:
    print('Os dois são iguais')
