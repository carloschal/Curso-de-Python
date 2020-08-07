print('Gerador de PA')
print('-='*10)
p = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
termo = p
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados'.format(tot))