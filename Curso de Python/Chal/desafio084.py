dado = list()
lista = list()
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    lista.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Os dados foram {lista}')
print(f'Foram cadastrados {len(lista)} pessoas. ')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in lista:
    if p[1] == mai:
       print(f'{p[0]}', end='')
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in lista:
    if p[1] == men:
       print(f'{p[0]}', end='')

