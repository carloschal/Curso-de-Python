def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {l} x {c} é {a}m².')


print('{:^30}'.format('Controle de Terrenos'))
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)