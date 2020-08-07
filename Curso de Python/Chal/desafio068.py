from random import  randint
v = 0
while True:
    j = int(input('Diga um valor: '))
    comp = randint(0, 10)
    tot = j + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {j} e o computador {comp}. Total de {tot} ')
    print('DEU PAR' if tot % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')




