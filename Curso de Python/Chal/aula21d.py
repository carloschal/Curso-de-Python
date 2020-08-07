def teste(b):#Escopo local
    global a
    a = 9
    b += a
    c = 4
    print(f'O valor de a dentro é {a}')
    print(f'O valor de b dentro é {b}')
    print(f'O valor de c dentro é {c}')


a = 2#Escopo global
teste(a)
print('-' * 15)
print(f'O valor de a fora é {a}')