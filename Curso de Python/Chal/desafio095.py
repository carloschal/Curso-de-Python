time = list()
jog = dict()
partidas = list()

while True:
    jog.clear()
    jog['nome'] = str(input('Nome do Jogador: ')).title()
    tot = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jog['gols'] = partidas[:]
    jog['total'] = sum(partidas)
    time.append(jog.copy())
    while True:
        resp = str(input('Quer continuar: [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{(k):>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador: (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<Volte Sempre>>')








