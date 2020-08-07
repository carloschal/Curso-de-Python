from time import sleep


def maior(*num):
    cont = maior = 0
    print('\nAnalizando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = maior
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print('-=' * 20)


# Programa principal
maior(2, 5, 6, 7, 9, 8)
maior(5, 6, 8, 9, 7)
maior(8, 7, 1, 2)
maior(4, 5, 6)


