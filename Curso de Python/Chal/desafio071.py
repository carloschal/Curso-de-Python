print('=' * 50)
print('\33[7m{:^50}\33[m'.format('BANCO BRADESCO'))
print('=' * 50)
cd = 'Cédulas disponíveis: 100, 50, 20, 10, 5 e 2.'
cs = 'Qual valor deseja sacar? R$'
print(f'\33[7m{cd:<50}\33[m')
print('=' * 50)
v = int(input(f'\33[7m{cs}\33[m'))
print('=' * 50)
if v % 2 == 1:
    print(f'\33[7m{cd:<50}\33[m')
    print('=' * 50)
    v = int(input(f'\33[7m{cs}\33[m'))
    print('=' * 50)
tot = v
ced = 100
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'\33[7mTotal de {totced} cédulas de {ced}\33[m')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        totced = 0
        if tot == 0:
            break
print('=' * 50)
print('{:^50}'.format('Volte Sempre, o Bradesco agradece! '))



