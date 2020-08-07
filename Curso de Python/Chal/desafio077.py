palavras = ('plenitude', 'gladiador', 'hegemonia', 'dicotomia', 'japonismo',
         'insofrido', 'habilitar', 'desdenhar', 'impetuoso', 'regozijar',
         'vacilador', 'agulheiro', 'balizador', 'carbonado', 'danificar',
         'entremesa', 'furibundo', 'lombalgia', 'modificar', 'torturado')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')