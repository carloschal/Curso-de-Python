lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores')
print(f'A lista de valores em ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado!')
