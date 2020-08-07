from random import  randint
n = (randint(1, 9), randint(1, 9), randint(1, 9),
     randint(1, 9), randint(1, 9))
print(f'Os valores sorteados foram: ', end='')
for num in n:
    print(f'{num}', end=' ')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')