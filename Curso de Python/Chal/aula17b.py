a = [2, 3, 4, 7]
#b = a#igual
b = a[:]#cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')