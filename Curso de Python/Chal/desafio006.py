n=int(input('Digite um número: '))
print('O número \033[35m{}\033[m tem como dobro \033[33m{}\033[m, triplo \033[36m{}\033[m e raiz quadrada {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))

