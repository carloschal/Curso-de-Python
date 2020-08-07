print('-=' * 20)
print('{:^40}'.format('Brasileirão'))
print('-=' * 20)
brasileirao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
               'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians',
               'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Ceará',
               'Atlético-MG', 'Fluminense', 'Botafogo', 'Cruzeiro',
               'CSA', 'Chapecoense', 'Avaí')
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-=' * 20)
print(f'Os 5 primeiros são: {brasileirao[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('-=' * 20)
print(sorted(brasileirao))
print('-=' * 20)
print(f'O Chapecoense está na {brasileirao.index("Chapecoense") + 1}ª posição')
print('-=' * 20)
print('Fim do Programa')

