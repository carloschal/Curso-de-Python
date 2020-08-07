r1 = float(input('Digite o primeiro segmento de reta: '))
r2 = float(input('Digite o segundo segmento de reta: '))
r3 = float(input('Digite o terceiro segmento de reta: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('\033[34mEquilátero!\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[35mEscaleno!\033[m')
    else:
        print('\033[33mIsósceles!\033[m')

else:
    print('Não formam um triângulo')
