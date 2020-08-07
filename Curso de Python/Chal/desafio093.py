jog = dict()
partidas = list()
jog['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas{jog["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
jog['gols'] = partidas[:]
jog['total'] = sum(partidas)
print('-=' * 30)
print(jog)
print('-=' * 30)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v} ')
print('-=' * 30)
print(f'O jogador {jog["nome"]} jogou {len(jog["gols"])} partidas')
for i, v in enumerate(jog['gols']):
    print(f'  =>Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jog["total"]} gols.')
