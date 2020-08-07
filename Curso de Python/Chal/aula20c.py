#empacotar parametos
def contador(* num):
    print(num)
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')
    tam = len(num)
    print(f'Recebi os valores{num} e são ao todo {tam} números')



contador(2, 1, 3)
contador(5, 6, 9, 8)
contador(3, 5)
