x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
z = int(input('Digite outro número: '))
if x < y and x < z:
    menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
if x > y and x > z:
    maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
