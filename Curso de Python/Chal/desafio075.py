n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
n = (n1, n2, n3, n4)
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vez(es)')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('não tem o número 3')
print('os valores pares digitados foram ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')