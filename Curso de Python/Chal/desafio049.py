n = int(input('Digite um número para ver sua tabuada: '))
print('-=' * 10)
print('A Tabuada de {}'.format(n))
print('-=' * 10)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print('-=' * 10)
print('Fim')
