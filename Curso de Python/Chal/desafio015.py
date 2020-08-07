d = int(input('\033[33mQuantos dias utilizou o veículo:\033[m '))
q = int(input('\033[33mQuantos quilometros percorreu:\033[m '))
t = (d*60)+(q*0.15)
print('O valor a ser pago é R$ \033[7;30m{:.2f}\033[m'.format(t))
