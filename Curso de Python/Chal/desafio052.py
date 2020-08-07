n = int(input('Digite um numero: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível por {} vezes.'.format(n, cont))
if cont == 2:
    print('E por isso ele é \033[34mPrimo.\033[m')
else:
    print('E por isso \033[34mnão é Primo.\033[m')
