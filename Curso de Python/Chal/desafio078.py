val = list()
for c in range(0, 5):
    val.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = val[c]
    else:
        if val[c] > mai:
            mai = val[c]
        if val[c] < men:
            men = val[c]
print('-=' * 30)
print(f'Você digitou os valores {val}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(val):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(val):
    if v == men:
        print(f'{i}...', end='')
print()

