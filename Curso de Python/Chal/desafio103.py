def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


print('-' * 20)
n = str(input('Nome do Jogador: ')).title()
g = str(input('Número de Gols: '))
print('-' * 20)
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

