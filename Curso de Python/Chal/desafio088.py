from random import randint
lista = list()
jogos = list()
print('-' * 40)
print('{:^40}'.format('JOGOS DAS LOTERIAS CAIXA'))
print('-' * 40)
print('''Escolha o jogo:
[ 1 ] Mega Sena
[ 2 ] Quina
[ 3 ] Lotofácil
[ 4 ] Lotomania
[ 5 ] Timemania''')
print('-' * 40)
opção = int(input('Sua opção: '))
print('-' * 40)
if opção == 1:
    quant = int(input('Quantos jogos serão sorteados? '))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            n = randint(1, 60)
            if n not in lista:
                lista.append(n)
                cont += 1
            if cont >= 6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print('-' * 10, f' SORTEANDO {quant} JOGOS DA MEGA SENA ', '-' * 9)
    for i, l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')
        print('-' * 40)
    print('{:^40}'.format('Boa Sorte'))
elif opção == 2:
    quant = int(input('Quantos jogos serão sorteados? '))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            n = randint(1, 80)
            if n not in lista:
                lista.append(n)
                cont += 1
            if cont >= 5:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print('-' * 10, f' SORTEANDO {quant} JOGOS DA QUINA ', '-' * 9)
    for i, l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')
    print('-' * 40)
    print('{:^40}'.format('Boa Sorte'))
elif opção == 3:
    quant = int(input('Quantos jogos serão sorteados? '))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            n = randint(1, 25)
            if n not in lista:
                lista.append(n)
                cont += 1
            if cont >= 15:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print('-' * 10, f' SORTEANDO {quant} JOGOS LOTOFÁCIL ', '-' * 9)
    for i, l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')
        print('-' * 40)
    print('{:^40}'.format('Boa Sorte'))
elif opção == 4:
    quant = int(input('Quantos jogos serão sorteados? '))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            n = randint(1, 99)
            if n not in lista:
                lista.append(n)
                cont += 1
            if cont >= 50:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print('-' * 10, f' SORTEANDO {quant} JOGOS LOTOMANIA ', '-=' * 9)
    for i, l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')
        print('-' * 40)
    print('{:^40}'.format('Boa Sorte'))
elif opção == 5:
    quant = int(input('Quantos jogos serão sorteados? '))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            n = randint(1, 80)
            if n not in lista:
                lista.append(n)
                cont += 1
            if cont >= 10:
                breakn
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print('-' * 10, f' SORTEANDO {quant} JOGOS TIMEMANIA ', '-' * 9)
    for i, l in enumerate(jogos):
        print(f'Jogo {i}: {l}')
        print('-' * 40)
    print('{:^40}'.format('Boa Sorte'))
else:
    print('Opção inválida. Tente novamente!')