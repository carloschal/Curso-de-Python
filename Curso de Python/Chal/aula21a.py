#Parâmetro adicional
#def somar(a, b, c=0):
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 4)
somar(4, 8)
somar()
somar(c=7, a=3)
