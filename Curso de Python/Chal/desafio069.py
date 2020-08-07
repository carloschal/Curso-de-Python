print('=' * 30)
print('{:^30}'.format('INÍCIO DO PROGRAMA'))
print('-' * 25)
print('{:^25}'.format('CADASTRE UMA PESSOA'))
print('-' * 25)
tot18 = totH = totF20 = 0
while True:
    id = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if id >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and id < 20:
        totF20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 25)
    if resp == 'N':
        break
print(f'Existem {tot18} pessoas com mais de 18 anos')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totF20} mulheres com menos de 20 anos')
print('-' * 25)
print('{:^25}'.format('FIM DO PROGRAMA'))
