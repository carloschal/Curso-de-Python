pessoas = {'nome': 'Carlos', 'sexo': 'M', 'idade': 44}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
pessoas['peso'] = 95.5 
for k in pessoas.keys():
    print(k)
print()
pessoas['nome'] = 'Leandro'
for k in pessoas.values():
    print(k)
print()
del pessoas['sexo']

for k, v in pessoas.items():
    print(f'{k} = {v}')