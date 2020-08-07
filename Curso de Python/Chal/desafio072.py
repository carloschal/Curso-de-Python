cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
      'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
      'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
      'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
      'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {cont[n]}')
    else:
        print('Tente novamente.')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 25)
    if resp == 'N':
        print('Agradeço sua participação!')
        break
