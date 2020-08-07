num = [2, 5, 9, 1]
num[2] = 3#trocar valores
num.append(7)#adicionar
#num.sort()#organizar
num.sort(reverse=True)#reverter organizando
num.insert(2, 0)#inseri elementos
#num.pop(2)#remover posição
#num.remove(2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')#número de elementos
