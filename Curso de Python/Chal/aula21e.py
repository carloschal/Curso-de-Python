def somar(a=0, b=0, c=0):
    s = a + b + c
    return s #comando return


r1 = somar(3, 2, 4)
r2 = somar(4, 8)
r3 = somar()
r4 = somar(c=7, a=3)
print(f'Meus cálculos deram {r1}, {r2}, {r3} e {r4}.')