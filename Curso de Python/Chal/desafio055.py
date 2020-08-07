maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('O peso da {}ª pessoa é: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))

