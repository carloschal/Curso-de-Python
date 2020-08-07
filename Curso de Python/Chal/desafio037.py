n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
e = int(input('Sua opção:'))
b = bin(n)
o = oct(n)
h = hex(n)
if e == 1:
    print('O Valor binário do número {} é de {}.'.format(n, b[2:]))
elif e == 2:
    print('O Valor octal do número {} é de {}.'.format(n, o[2:]))
elif e == 3:
    print('O valor hexadecimal do número {} é de {}.'.format(n, h[2:]))
else:
    print('Opção inválida. Tente novamente.')
