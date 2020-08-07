from desafio112.utilidadescev import moeda
from desafio112.utilidadescev import dados

p = dados.leiaDinheiro('Digite o preço: R$')
a = int(input('Digite a taxa de acréscimo: '))
d = int(input('Digite a taxa de desconto: '))
moeda.resumo(p, a, d)
