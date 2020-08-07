import random
n1 = input('Digite o seu nome: ')
n2 = input('Digite o seu nome: ')
n3 = input('Digite o seu nome: ')
n4 = input('Digite o seu nome: ')
lista = (n1, n2, n3, n4)
escolhido = random.choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))